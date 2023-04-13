from django.contrib import admin
from django.urls import path, include

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/threadlist/', ThreadListCreateAPIView.as_view()),
    path('api/v1/threadlist/<int:pk>/', ThreadDetailAPIView.as_view()),
    path('api/v1/threadlist/<int:pk>/detail/', message_detail),
    path('api/v1/messagelist/<int:pk>/', MessageReadAPIView.as_view()),
    path('api/v1/messagelist/', MessageCountAPIView.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls'))
]
