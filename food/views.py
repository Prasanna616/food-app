from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

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

def item(request):
    return HttpResponse('<h1> This is item list! </h1>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    #return HttpResponse("This is item_id: %s" % item_id)
    return render(request,'food/detail.html',context)