from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ItemForm

# Create your views here.

def index(request):
    # item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    # context ={
    #     'item_list':item_list
    # }
    # return HttpResponse(template.render(context,request))

    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }
    return render(request, 'food/index.html', context)

class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html';
    context_object_name = 'item_list';

def item(request):
    return HttpResponse('<h1> This is item list! </h1>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    #return HttpResponse("This is item_id: %s" % item_id)
    return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    model = Item;
    template_name = 'food/detail.html';

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})
    

def delete_item(request, id):
    item = Item.objects.get(id=id);

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html',{'item':item})
