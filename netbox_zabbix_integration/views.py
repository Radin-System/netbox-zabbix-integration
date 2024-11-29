from netbox.views import generic
from . import models, tables

class ZabbixReletionshipView(generic.ObjectView):
    queryset = models.ZabbixRelationship.objects.all()

class ZabbixReletionshipListView(generic.ObjectView):
    queryset = models.ZabbixRelationship.objects.all()
    table = tables.ZabbixRelationshipTable
