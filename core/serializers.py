from rest_framework import serializers
from .models import (
    CustomUser,
    Currency,
    HistoryEvent,
    ClientOperation,
    Shift
)
from django.utils import timezone

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'created_at', 'balance']


# serializers.py

# serializers.py

# serializers.py
from rest_framework import serializers
from .models import HistoryEvent, CustomUser, Currency

class HistoryEventSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    target_user = serializers.SerializerMethodField()
    currency = serializers.StringRelatedField()
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = HistoryEvent
        fields = ['id', 'event_type', 'user', 'target_user', 'currency', 'timestamp']

    def get_user(self, obj):
        if obj.user:
            return f"{obj.user.username} (ID: {obj.user.id})"
        return "N/A"

    def get_target_user(self, obj):
        if obj.target_user:
            return f"{obj.target_user.username} (ID: {obj.target_user.id})"
        return "N/A"

    def get_timestamp(self, obj):
        return obj.timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')



class ClientOperationSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()
    currency_name = serializers.CharField(source='currency.name', read_only=True)  # Новое поле

    class Meta:
        model = ClientOperation
        fields = [
            'id',
            'operation_type',
            'currency',
            'currency_name',
            'cashier_name',
            'amount',
            'exchange_rate',
            'total_in_som',
            'timestamp',
            'edited'
        ]

    def get_timestamp(self, obj):
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')



class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'user', 'start_time', 'end_time', 'note']



from rest_framework import serializers
from .models import Shift


class ShiftHistorySerializer(serializers.ModelSerializer):
    cashier_name = serializers.SerializerMethodField()
    operations_count = serializers.IntegerField()
    overall_profit = serializers.DecimalField(max_digits=15, decimal_places=2)
    changed_balances = serializers.JSONField()  # already stored in shift

    class Meta:
        model = Shift
        fields = [
            'id',
            'cashier_name',
            'start_time',
            'end_time',
            'operations_count',
            'overall_profit',
            'changed_balances',
        ]

    def get_cashier_name(self, obj):
        return obj.user.username if obj.user else "No cashier"

