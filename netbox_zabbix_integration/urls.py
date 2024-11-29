from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('zabbix-relationship/', views.ZabbixRelationshipListView.as_view(), name='zabbix_relationship_list'),
    path('zabbix-relationship/add/', views.ZabbixRelationshipEditView.as_view(), name='zabbix_relationship_add'),
    path('zabbix-relationship/<int:pk>/', views.ZabbixRelationshipView.as_view(), name='zabbix_relationship'),
    path('zabbix-relationship/<int:pk>/edit/', views.ZabbixRelationshipEditView.as_view(), name='zabbix_relationship_edit'),
    path('zabbix-relationship/<int:pk>/delete/', views.ZabbixRelationshipDeleteView.as_view(), name='zabbix_relationship_delete'),
    path('zabbix-relationship/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='zabbix_relationship_changelog', kwargs={
        'model': models.ZabbixRelationship
    }),
)
