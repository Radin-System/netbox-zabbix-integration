import django_tables2 as tables

from netbox.tables import NetBoxTable
from netbox_zabbix_integration.models import ZabbixRelationship

class ZabbixRelationshipTable(NetBoxTable):
    assigned_object = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = ZabbixRelationship
        fields = ('pk', 'id', 'assigned_object', 'zabbix_model', 'zabbix_id', 'zabbix_name')
        default_columns = ('assigned_object', 'zabbix_model', 'zabbix_name')