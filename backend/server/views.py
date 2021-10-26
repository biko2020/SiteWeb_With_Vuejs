from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from server.settings import DATABASES



def index(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'email': email,
            'subject': subject,
            'message': message 
        }
        message ='''
        Message : {}
        Envoyer par : {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '',['brahimlion38@gmail.com'])
    return render(request, 'http://127.0.0.1:8080/src/components/ContactApp.vue', {})