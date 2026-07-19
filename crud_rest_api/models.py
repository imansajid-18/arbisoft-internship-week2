from django.contrib.auth.models import User
from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

