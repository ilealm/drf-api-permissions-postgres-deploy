
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsAuthorOrReadOnly


class CoursesList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CoursesDetail(RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
