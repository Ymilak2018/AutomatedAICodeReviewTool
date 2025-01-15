from django.urls import path
from .views import Home, CB
urlpatterns = [
    path('', Home),
    path('chatbot/', CB)
]