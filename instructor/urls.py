from django.urls import path
from .views import upload_lecture, schedule

app_name = 'instructor'

urlpatterns = [
    path('upload/', upload_lecture, name='upload_lecture'),
    path('schedule/', schedule, name='schedule'),
]
