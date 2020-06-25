from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','owner','title','start_date', 'end_date', 'age_range', 'is_outdoors','description',)
