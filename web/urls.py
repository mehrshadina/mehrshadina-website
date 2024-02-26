from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('donate/', donate, name='donate'),
    path('project_order/', project_order, name='project-order'),
    path('tutoring/', tutoring, name='tutoring'),
    path('projects/', projects, name='projects'),
    path('submit/project/', create_project, name='submit_project'),
]