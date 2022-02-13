from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('pages/', name),
    path('repetitors/', categories),
    path('', main),
]
