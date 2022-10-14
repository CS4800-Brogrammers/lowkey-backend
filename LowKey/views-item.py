from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .forms import ItemForm
from .models import Item

#requires you to be logged in to create room / else be redirected
def allItems(request):
    items_all = Item.objects.all()
    context = {'items_all':items_all}
    return JsonResponse(context)

@login_required(login_url = 'login')
def createItem(request):
    form = ItemForm()

    if request.method == 'POST':
        #topic_name = request.POST.get('topic')
        #topic, created = Topic.objects.get_or_create(name = topic_name)
        Item.objects.create(
            owner = request.user,
            #topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
        )
        #return redirect('home')
        pass

def getItem(request, pk):
    item = Item.objects.get(id=pk)
    context = {'item':item}
    return JsonResponse(context)

@login_required(login_url = 'login')
def updateItem(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance = item)
    #topics = Topic.objects.all()
    #only room host should be able to edit 
    if request.user != item.owner:
        return HttpResponse('You are not allowed here!!')

    if request.method == "POST":
        #topic_name = request.POST.get('topic')
        #topic, created = Topic.objects.get_or_create(name = topic_name)
        item.name = request.POST.get('name')
        #item.topic = topic
        item.description = request.POST.get('description')
        item.save()

        #return redirect('home')
        pass

    context = {'form': form, 'item': item}
    #return render(request, 'base/room_form.html', context)
    pass

@login_required(login_url = 'login')
def deleteItem(request, pk):
    item = Item.objects.get(id = pk)

    if request.user != item.owner:
        return HttpResponse('You are not allowed here!!')

    if request.method == "POST":
        item.delete()
        #return redirect('home')
        
    #return render(request, 'base/delete.html',{'obj':room})
    pass