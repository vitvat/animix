from django.urls import path
from .views import filter_mother_choices

urlpatterns = [
    path('filter_mother_choices/', filter_mother_choices, name='filter_mother_choices'),
]
