from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Thread, Message


class ThreadSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Thread
        fields = ('id', 'participants')
