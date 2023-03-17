from django.contrib import admin
from django.urls import path, include
from chatbot_app import views

urlpatterns = [
    path("",views.home,name='chatbot'),
    path("chatbot",views.chatbot,name='chatbot'),
    path("home",views.home,name='chatbot'),
    path("#",views.contact_us,name='chatbot')
]
   