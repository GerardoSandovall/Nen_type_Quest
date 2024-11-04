from django.db import models
from django.contrib.auth.models import User

class NenPoints(models.Model):
    Enhancer = models.IntegerField(default=0)
    Transmutator = models.IntegerField(default=0)
    Emitter = models.IntegerField(default=0)
    Conjurer = models.IntegerField(default=0)
    Manipulator = models.IntegerField(default=0)
    Specialist = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answered_fiel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Nen Points"