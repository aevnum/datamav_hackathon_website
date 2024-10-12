from django.db import models
from users.models import CustomUser

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(CustomUser, related_name='teams')  # Unique related name here

    def __str__(self):
        return self.name
