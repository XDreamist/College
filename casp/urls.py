from django.urls import path

from casp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('registration', views.registration, name="registration"),
    path('viewteachers', views.viewTeachers, name="viewteachers")
]