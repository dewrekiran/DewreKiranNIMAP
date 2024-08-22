from django.urls import path
from .views import ClientListCreate, ClientRetrieveUpdateDestroy, ProjectListCreate, ProjectAssignToClient

urlpatterns = [
    path('clients/', ClientListCreate.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroy.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectAssignToClient.as_view(), name='project-assign'),
    path('projects/', ProjectListCreate.as_view(), name='project-list-create'),
]
