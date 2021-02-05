from django.db import models

# Create your models here.
class Todo(models.Model):
    list_text = models.CharField(max_length=200)
    date = models.DateTimeField()