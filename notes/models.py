from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

COLORS = [
    ("white", "White"),
    ("black", "Black"),
    ("yellow", "Yellow"),
    ("orange", "Orange"),
    ("green", "Green"),
    ("red", "Red"),
    ("blue", "Blue"),
    ("pink", "Pink"),
]


class TimeStampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Note(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    color = models.CharField(max_length=50, choices=COLORS, default="white")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title