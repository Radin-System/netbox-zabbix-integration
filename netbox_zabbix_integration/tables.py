import django_tables2 as tables

from netbox.tables import NetBoxTable
from netbox_zabbix_integration.models import Relationship

class RelationshipTable(NetBoxTable):
    assigned_object = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = Relationship
        fields = ('pk', 'id', 'content_type', 'assigned_object', 'zabbix_model', 'zabbix_id', 'zabbix_name', 'status')
        default_columns = ('assigned_object', 'zabbix_model', 'zabbix_name')
        exclude = ('actions',)