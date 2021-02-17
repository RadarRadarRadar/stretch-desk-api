from django.db import models
from django.contrib.auth import get_user_model

class Stretch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video = models.TextField()
    instructions = models.TextField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Try out {self.name}!"

    def as_dict(self):
        """returns a dict of the Stretch models"""
        return {
            'id': self.id,
            'description': self.description,
            'video': self.video,
            'instructions': self.instructions
        }
