from netbox.forms import NetBoxModelForm
from .models import ZabbixRelationship

class ZabbixRelationshipForm(NetBoxModelForm):

    class Meta:
        model = ZabbixRelationship
        fields = ()