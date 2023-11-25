from django.urls import path
from . import views

urlpatterns = [
    path('',views.show),
    path('autoid/',views.show2, name='autoid'),
]
