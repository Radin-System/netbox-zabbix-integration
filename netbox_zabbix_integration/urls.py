from django.urls import path
from .views import *

app_name = 'zabbix_integration'

urlpatterns = (
    path('zabbix-status/', ZabbixStatusView.as_view(), name='zabbix-status'),

    path('relationship/', RelationshipListView.as_view(), name='relationship_list'),
    path('relationship/<int:pk>/', RelationshipView.as_view(), name='relationship'),
)
