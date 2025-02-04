
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('cashier', 'Cashier'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cashier')

    # Add is_deleted field
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    # Add is_deleted field
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HistoryEvent(models.Model):
    EVENT_TYPES = [
        ('create_user', 'Create User'),
        ('delete_user', 'Delete User'),
        ('update_user', 'Update User'),
        ('create_currency', 'Create Currency'),
        ('delete_currency', 'Delete Currency'),
        ('update_currency', 'Update Currency'),
    ]

    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    user = models.ForeignKey(CustomUser, related_name='performed_events', on_delete=models.SET_NULL, null=True, blank=True)
    target_user = models.ForeignKey(CustomUser, related_name='targeted_events', on_delete=models.SET_NULL, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_event_type_display()} by {self.user} on {self.timestamp}"


class ClientOperation(models.Model):
    OPERATION_TYPE_CHOICES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )

    operation_type = models.CharField(max_length=10, choices=OPERATION_TYPE_CHOICES)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    # Вместо user-ссылки:
    cashier_name = models.CharField(max_length=150, default='')  # Новое поле
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    total_in_som = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # Новое поле
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.CharField(max_length=150, blank=True, default='')
    def __str__(self):
        return f"{self.operation_type} {self.currency.name} {self.amount}"


class Shift(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    note = models.TextField(blank=True, null=True)
    changed_balances = models.JSONField(blank=True, null=True)  # Новое поле

    def __str__(self):
        return f"Shift (id={self.id}) - {self.user} from {self.start_time} to {self.end_time}"


from rest_framework import viewsets
from .serializers import CurrencySerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['notification'] = f"Валюта '{response.data['name']}' успешно создана!"
        return response



