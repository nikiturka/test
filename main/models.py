from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Thread(models.Model):
    participants = models.ManyToManyField(User, limit_choices_to={'thread__lt': 2})
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Message(models.Model):
    # deleting all the messages from users that do not exist
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)  # deleting thread with user that do not exist
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.text
