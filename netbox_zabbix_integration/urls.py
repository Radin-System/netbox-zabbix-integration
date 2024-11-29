from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('zabbix-integration/', views.ZabbixRelationshipListView.as_view(), name='zabbix_relationship_list'),
    path('zabbix-integration/add/', views.ZabbixRelationshipEditView.as_view(), name='zabbix_relationship_add'),
    path('zabbix-integration/<int:pk>/', views.ZabbixRelationshipView.as_view(), name='zabbix_relationship'),
    path('zabbix-integration/<int:pk>/edit/', views.ZabbixRelationshipEditView.as_view(), name='zabbixrelationship_edit'),
    path('zabbix-integration/<int:pk>/delete/', views.ZabbixRelationshipDeleteView.as_view(), name='zabbix_relationship_delete'),
    path('zabbix-integration/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='zabbix_relationship_changelog', kwargs={
        'model': models.ZabbixRelationship
    }),
)
