from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    path('project-order/', views.project_order, name='project-order'),
    path('tutoring/', views.tutoring, name='tutoring'),
    path('projects/', views.projects, name='projects'),

    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('submit/income/', views.submit_income, name='income'),
]
