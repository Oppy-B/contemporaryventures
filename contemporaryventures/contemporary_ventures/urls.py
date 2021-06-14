from django.urls import path
from . import views


app_name = 'contemporary_ventures'

urlpatterns = [
    path("", views.cv_index, name = "cv_index"),
    path("about-us/", views.about_us, name = "about_us"),
    path("contact/", views.contact, name = "contact"),
    path("project-apartment-cleaning/", views.proj_apartment_cleaning, name = "proj_apartment_cleaning"),
    path("project/", views.project, name = "project"),
    path("project-after-renovation-cleaning/", views.project_after_renovation_cleaning, name = "project_after_renovation_cleaning"),
    path("service-house-cleaning/", views.service_house_cleaning, name = "service_house_cleaning"),
    path("services/", views.services, name = "services"),
    path("service-post-renovation/", views.service_post_renovation, name = "service_post_renovation"),
    path("service-commercial-cleaning/", views.service_commercial_cleaning, name = "service_commercial_cleaning"),
    path("service-window-cleaning/", views.service_window_cleaning, name = "service_window_cleaning"),
]