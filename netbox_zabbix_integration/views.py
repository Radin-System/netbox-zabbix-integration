from netbox.views import generic
from . import models, tables, forms

class ZabbixRelationshipView(generic.ObjectView):
    queryset = models.ZabbixRelationship.objects.all()

class ZabbixRelationshipListView(generic.ObjectListView):
    queryset = models.ZabbixRelationship.objects.all()
    table = tables.ZabbixRelationshipTable

class ZabbixRelationshipEditView(generic.ObjectEditView):
    queryset = models.ZabbixRelationship.objects.all()
    form = forms.ZabbixRelationshipForm

class ZabbixRelationshipDeleteView(generic.ObjectDeleteView):
    queryset = models.ZabbixRelationship.objects.all()