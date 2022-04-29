from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Item
# Create your views here.
def index(request):
    return render(request, 'list/index.html', {
        'list': Item.objects.order_by('time_posted')[:5]
    })

def create(request):
    return HttpResponse()

def view(request, id):
    items = Item.objects.order_by('time_posted')[:5]
    output = ', '.join([q.text for q in items])
    return HttpResponse(output)