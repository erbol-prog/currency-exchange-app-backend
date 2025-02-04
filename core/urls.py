from rest_framework import routers

from .views import (
    CurrencyViewSet,
    ClientOperationViewSet,
    ShiftViewSet,
    CustomUserViewSet,
    HistoryEventViewSet,
    AnalyticsView,
    AdvancedAnalyticsView,
    ExportEventExcel,
    ExportOperationExcel,
    ExportAnalyticsExcel, InternalHistoryAPIView
    # <и т.д.>
)

from django.urls import path, include
from .views import (
    # your other viewsets,
    ShiftViewSet,
    # ...
)


router = routers.DefaultRouter()
router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'operations', ClientOperationViewSet, basename='operation')
router.register(r'shifts', ShiftViewSet, basename='shift')
router.register(r'histories', HistoryEventViewSet, basename='histories')
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('events/export_excel/', ExportEventExcel.as_view(), name='export-event-excel'),
    path('operations/export_excel/', ExportOperationExcel.as_view(), name='export-operation-excel'),
    path('analytics/export_excel/', ExportAnalyticsExcel.as_view(), name='export-analytics-excel'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('analytics/advanced/', AdvancedAnalyticsView.as_view(), name='analytics-advanced'),
    path('internal-history/', InternalHistoryAPIView.as_view(), name='internal-history'),
    path('', include(router.urls)),
]
