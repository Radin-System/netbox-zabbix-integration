from netbox.forms import NetBoxModelForm
from .models import Relationship

class RelationshipForm(NetBoxModelForm):

    class Meta:
        model = Relationship
        fields = ()