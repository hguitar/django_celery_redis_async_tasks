from django.shortcuts import render
from django.http import HttpResponse
from .tasks import task_send_email

# Create your views here.
def index(request):
    task_send_email.delay()
    return HttpResponse('Done')