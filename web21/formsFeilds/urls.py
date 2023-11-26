from django.urls import path
from . import views
urlpatterns = [
    path('',views.show),
    path('success/', views.success, name='successPage'),
]
