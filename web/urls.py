from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('submit/income/', views.submit_income, name='income'),
]
