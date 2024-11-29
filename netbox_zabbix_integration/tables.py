import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from netbox_zabbix_integration.models import Relationship

class RelationshipTable(NetBoxTable):
    id = tables.Column(
        linkify=False,
    )

    assigned_object = tables.Column(
        linkify=True,
    )

    status = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = Relationship
        fields = ('pk', 'id', 'content_type', 'assigned_object', 'zabbix_id', 'zabbix_model', 'zabbix_object', 'status')
        default_columns = ('assigned_object', 'zabbix_model', 'zabbix_name')
        exclude = ('actions',)