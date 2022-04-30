from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

from .models import User, Item
# Create your views here.
def index(request):
    return render(request, 'list/index.html', {
        'list': Item.objects.order_by('time_posted')
    })

def create(request):
    if request.method == "POST":
        data = request.POST
        if (len(data.get('text')) < 1):
            return render(request, 'list/create.html', {
            'list': Item.objects.order_by('time_posted'),
            'error': 'Your text must have 1+ characters'
        })
        else:
            toSave = Item(text=data.get('text'), author=request.user)
            toSave.save()
    return render(request, 'list/create.html', {
        'list': Item.objects.order_by('time_posted')
    })

def view(request, id):
    items = Item.objects.order_by('time_posted')[:5]
    output = ', '.join([q.text for q in items])
    return HttpResponse(output)