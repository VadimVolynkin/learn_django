from django.urls import path

from . views import list_person

urlpatterns = [
    path('list', list_person),
]
