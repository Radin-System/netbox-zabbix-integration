from django.urls import path
from .views import relationship

app_name = 'zabbix_integration'

urlpatterns = (
    path('zabbix-status/', relationship.ZabbixStatusView.as_view(), name='zabbix-status'),

    path('relationship/', relationship.RelationshipListView.as_view(), name='relationship_list'),
    path('relationship/<int:pk>/', relationship.RelationshipView.as_view(), name='relationship'),
)
