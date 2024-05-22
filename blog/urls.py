from . import views
from django.urls import path


urlpatterns = [
    path('', views.DoctorList.as_view(), name='home'),
]
