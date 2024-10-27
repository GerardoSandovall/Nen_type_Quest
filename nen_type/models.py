from django.db import models
from django.contrib.auth.models import User

class NenPoints(models.Model):
    Enhancer = models.IntegerField()
    Transmutator = models.IntegerField()
    Emitter = models.IntegerField()
    Conjurer = models.IntegerField()
    Manipulator = models.IntegerField()
    Specialist = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - Nen Points"