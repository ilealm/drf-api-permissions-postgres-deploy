from django.urls import path
from .views import CoursesList, CoursesDetail

urlpatterns = [
    path('', CoursesList.as_view(), name='courses_list'),
    path('<int:pk>/', CoursesDetail.as_view(), name='courses_detail'),
]
