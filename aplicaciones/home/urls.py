from django.urls import  path, re_path

from . import views

app_name = "homae_app"

urlpatterns = [
    path("nueva-url", views.IndexView.as_view(), name="index")
]