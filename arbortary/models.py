from wsgiref.handlers import format_date_time
from django.conf import settings
from django.db import models
from login.models import User
# Create your models here.


class Tree(models.Model):
    spiecie = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    reason = models.TextField()
    date_planted = models.DateField()
    visited_by = models.ManyToManyField(
        User, related_name='visited_trees')
    planted_by = models.ForeignKey(
        User, related_name='trees', on_delete=models.CASCADE)
