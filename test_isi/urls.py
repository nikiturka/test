from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/threadlist/', ThreadListCreateAPIView.as_view()),
]
