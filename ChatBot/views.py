from django.shortcuts import render
from .forms import CBform
from .models import Message
from .cb import ChatBotResponse
import re

# Create your views here.

def Home(request):

    return render(request, 'CB/homepage.html')

def CB(request):
    chatbot = CBform(request.POST or None)
    if chatbot.is_valid():
        chatbot.save()
        chatbot = CBform()

    last_message = Message.objects.all().order_by('-id').first()

    if last_message:
        ip_txt = last_message.inp_text
        op_txt = ChatBotResponse(ip_txt)
        response = op_txt
    else:
        ip_txt = 'No Chats till Now!'
        response = 'No Chats till Now!'

    response = [i for i in response.split('\n')]

    ctx = {
        'request': chatbot,
        'response': response,
        'ip': ip_txt
    }

    return render(request, 'CB/chatbotpage.html', ctx)
