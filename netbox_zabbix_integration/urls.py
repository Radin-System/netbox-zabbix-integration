from django.urls import path
from . import views

urlpatterns = (
    path('relationship/', views.RelationshipListView.as_view(), name='relationship_list'),
    path('relationship/<int:pk>/', views.RelationshipView.as_view(), name='relationship'),
)
