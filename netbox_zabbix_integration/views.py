from netbox.views import generic
from . import models, tables

class RelationshipView(generic.ObjectView):
    queryset = models.Relationship.objects.all()

class RelationshipListView(generic.ObjectListView):
    queryset = models.Relationship.objects.all()
    table = tables.RelationshipTable
