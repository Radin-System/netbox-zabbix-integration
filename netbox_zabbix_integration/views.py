from netbox.views import generic
from . import models, tables, forms

class RelationshipView(generic.ObjectView):
    queryset = models.Relationship.objects.all()

class RelationshipListView(generic.ObjectListView):
    queryset = models.Relationship.objects.all()
    table = tables.ZabbixRelationshipTable

class RelationshipEditView(generic.ObjectEditView):
    queryset = models.Relationship.objects.all()
    form = forms.RelationshipForm

class RelationshipDeleteView(generic.ObjectDeleteView):
    queryset = models.Relationship.objects.all()