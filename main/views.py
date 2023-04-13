from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Thread, Message
from .serializers import ThreadSerializer


class ThreadListCreateAPIView(generics.ListCreateAPIView):  # Create (Task 1) and List of threads for each user (Task 3)
    serializer_class = ThreadSerializer
    model = Thread

    def get_queryset(self):
        user = self.request.user.id
        print(user)
        return Thread.objects.filter(participants=user)


class ThreadDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer




