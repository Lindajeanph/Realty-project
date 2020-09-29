from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='happ_home'),
    path('my_profile/', views.create_the_happ_user, name='happ_my_profile'),
    path('survey/', views.dailysurvey, name='happ_survey'),
]