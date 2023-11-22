from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='home'),
    path('courses/',views.showCourseDetails,name='courses'),
    path('registration/',views.coursesRegistration,name='registration'),
    path('courses/<int:id>/update/', views.update_course, name='update'),
    path('courses/<int:id>/delete/', views.delete_course, name='delete'),
]
