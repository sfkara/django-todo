from django.db import models

# Create your models here.


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(max_length=40)

    def __str__(self):
        return self.text
