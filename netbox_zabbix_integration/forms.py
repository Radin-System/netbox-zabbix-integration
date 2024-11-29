from netbox.forms import NetBoxModelForm
from .models import ZabbixRelationship

class ZabbixRelationshipForm(NetBoxModelForm):

    class Meta:
        model = ZabbixRelationship
        fields = ('content_type', 'assigned_object', 'zabbix_model', 'zabbix_id', 'zabbix_name', 'status')