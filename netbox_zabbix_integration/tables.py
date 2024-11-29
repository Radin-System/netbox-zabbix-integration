import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_zabbix_integration.models import ZabbixRelationship

class ZabbixRelationshipTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    default_action = ChoiceFieldColumn()
    object_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = ZabbixRelationship
        fields = ('pk', 'id', 'assigned_object', 'zabbix_model', 'zabbix_id', 'zabbix_name')
        default_columns = ('assigned_object', 'zabbix_name')