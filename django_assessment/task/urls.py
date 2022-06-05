from django.urls import path
from . import views

urlpatterns = [
    path('new', views.create_new_record, name="create_new_record"),
    path('all', views.display_all_record, name="display_all_record"),

]
