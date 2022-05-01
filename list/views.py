from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Item, List

from .models import User, Item
# Create your views here.
def index(request):
    return render(request, 'list/index.html', {
        'list': List.objects.all()
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
            toSave = List(title=data.get('text'), author=request.user)
            toSave.save()
            #return redirect('/view/'+str(toSave.id), obj=toSave)
            return redirect('view', id=toSave.id)
    return render(request, 'list/create.html', {
        'list': Item.objects.order_by('time_posted')
    })

def view(request, id):
    if request.method == "POST":
        data = request.POST
        gotList = List.objects.get(id=id)
        if gotList:
            newItem = Item(text=data.get('text'))
            newItem.save()
            gotList.items.add(newItem)
            return render(request, 'list/view.html', {
            'obj': gotList,
            'items': gotList.items.all(),
            'canEdit': canEditList(gotList, request.user)

        }) 
        else:
            return HttpResponse("Error 404")
    item = get_object_or_404(List, id=id)

    return render(request, 'list/view.html', {
        'obj': item,
        'items': item.items.all(),
        'canEdit': canEditList(item, request.user)

    })

def getListFromUser(request, id):
    print("id: "+ str(id))
    data = List.objects.filter(author=User.objects.get(pk=id))
    return render(request, 'list/yourLists.html', {
        'lists': data,
        'user': request.user
    })

def canEditList(list, user):
    if list.author == user:
        return True

def deletelist(request, id):
    return HttpResponse(request.POST['text'])