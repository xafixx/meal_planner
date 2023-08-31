from django.urls import path
from . import views

app_name = "mealplanner_app"

urlpatterns = [
    path('', views.index, name='index'),
]