from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Item
from .forms import ItemForm

# Create your views here.
def home(request):
    items=Item.objects.all()
    total_cost=0
    for item in items:
        total_cost+=item.cost
    context={
        'items':items,
        'total_cost':total_cost
    }


    return render(request,'notes/index.html',context)

def create_item(request):
    
    if request.method=='POST':
        print("inside the post")
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ItemForm()
        print("inside the get request")
    context={
        'form':form,
        'action_url': reverse('create-item'),
    }
    
    return render(request,'notes/item_form.html',context)

def update_item(request,pk):
    #item=Item.objects.get(id=pk)
    item = get_object_or_404(Item, id=pk)
   
    if request.method=='POST':
        form=ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
         form=ItemForm(instance=item)

    context={
        'form':form,
        'action_url': reverse('update-item',args=[pk]),
        'item':item

    }
    return render(request,'notes/item_form.html',context)

def delete_item(request, pk):
    item = get_object_or_404(Item, id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('home')
    context={
        'item': item,
        'action_url': reverse('delete-item', args=[pk])
    }

    return render(request, 'notes/item_delete.html', context)