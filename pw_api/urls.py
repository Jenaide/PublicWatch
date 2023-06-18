from django.urls import path
from . import views

urlpatterns = [
    path('missing', views.list_missing_persons),
    path('mostwanted', views.list_most_wanted),
    path('missing/<int:id>', views.missing_person_details),
    path('mostwanted/<int:id>', views.wanted_person_details)
]