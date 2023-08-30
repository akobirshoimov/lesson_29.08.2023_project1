from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def detail(request,school_id):
    return HttpResponse(f'you ara loking at {school_id}')
def all_info(request):
    return HttpResponse('all info!')