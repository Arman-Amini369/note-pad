from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note")
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_pin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_pin']

    def __str__(self):
        return self.title