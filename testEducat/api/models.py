from django.db import models

class TaskItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()