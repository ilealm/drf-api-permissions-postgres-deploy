from django.contrib.auth import get_user_model
from django.db import models

class Course(models.Model):
    RANGE_CHOICES = (
        ('1', '3-5 years'),
        ('2', '6-8 years'),
        ('3', '9-12 years'),
        ('4', '13-16 years'),
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    age_range = models.CharField(max_length=1, choices=RANGE_CHOICES)
    is_outdoors = models.BooleanField(default=False)
    description = models.TextField()
