from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('relationship/', views.RelationshipListView.as_view(), name='relationship_list'),
    path('relationship/add/', views.RelationshipEditView.as_view(), name='relationship_add'),
    path('relationship/<int:pk>/', views.RelationshipView.as_view(), name='relationship'),
    path('relationship/<int:pk>/edit/', views.RelationshipEditView.as_view(), name='relationship_edit'),
    path('relationship/<int:pk>/delete/', views.RelationshipDeleteView.as_view(), name='relationship_delete'),
    path('relationship/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='relationship_changelog', kwargs={
        'model': models.Relationship
    }),
)
