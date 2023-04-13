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


@api_view(['GET', 'POST'])
def message_detail(request, pk):
    if request.method == 'GET':
        message = Message.objects.filter(thread=pk)
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

