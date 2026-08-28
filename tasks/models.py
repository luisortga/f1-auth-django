from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Pilot(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    team = models.CharField(max_length=80)
    track = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' - by ' + self.user.username
