from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    classes = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name