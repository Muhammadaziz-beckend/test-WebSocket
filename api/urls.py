from django.urls import path
from .views import MessageAPIView

urlpatterns = [
    path('api/message/', MessageAPIView.as_view(), name='message_api'),
]
