from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (
    path('zabbix-intgration/', views.ZabbixReletionshipListView.as_view(), name='zabbix_reletaionship_list'),
    path('zabbix-intgration/<int:pk>/', views.ZabbixReletionshipView.as_view(), name='zabbix_reletaionship'),
)

urlpatterns = (
    # Zabbix ReletaionShip
    # ...
    path('zabbix-intgration/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='zabbix_reletaionship_changelog', kwargs={
        'model': models.ZabbixRelationship
    }),
)