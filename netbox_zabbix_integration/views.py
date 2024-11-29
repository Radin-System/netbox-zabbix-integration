from netbox.views import generic
from . import models, tables

class ZabbixRelationshipView(generic.ObjectView):
    queryset = models.ZabbixRelationship.objects.all()

class ZabbixRelationshipListView(generic.ObjectListView):
    queryset = models.ZabbixRelationship.objects.all()
    table = tables.ZabbixRelationshipTable