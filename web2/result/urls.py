from django.urls import path
from . import views  # '.' represents current directory

urlpatterns = [
    path('result/',views.result),
]
