import hmac
import subprocess
import os
import hashlib
from dotenv import load_dotenv # type: ignore
load_dotenv('/home/pkweb/food-app/.env')

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import redirect, render   
from django.http import HttpResponse, HttpResponseForbidden
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import ItemForm
from django.contrib.auth.decorators import login_required #Redirects to Login if user is not authenticated
from django.contrib.auth.mixins import LoginRequiredMixin #Redirects to Login if user is not authenticated 

# Create your views here.
@csrf_exempt
def github_webhook(request):
    print(request.method)
    if request.method != 'POST':
        return HttpResponse('Method not allowed', status=405)
    
    #Step1: Validate the signature 
    github_signature = request.headers.get('X-hub-Signature-256')
    if not github_signature:
        return HttpResponseForbidden('Signature missing')
    
    sha_name, signature = github_signature.split('=')
    if sha_name != 'sha256':
        return HttpResponseForbidden('Invalid signature format')
    
    #Load the secret from settings or environment 
    #secret = settings.GITHUB_WEBHOOK_SECRET.encode()
    secret = os.getenv('GITHUB_WEBHOOK_SECRET')
    print(f"Secret:{secret}")

    #Generate hmac using request body
    mac = hmac.new(secret, msg=request.body, digestmod=hashlib.sha256)

    if not hmac.compare_digest(mac.hexdigest(),signature):
        return HttpResponseForbidden('Invalid signature')
    
    #Step2: run deploy script
    try:
        print(os.getcwd())
        subprocess.run(['bash','/home/pkweb/food-app/food/deploy.sh'], check=True)
        return HttpResponse('Secure deployment triggered')
    except subprocess.CalledProcessError as e:
        return HttpResponse(f'Deployment failed:{str(e)}',status= 500)


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
    template_name = 'food/index1.html';
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

class CreateItem(LoginRequiredMixin, CreateView):
    model = Item;
    fields = ['item_name','item_des','item_price','item_image']
    template_name = 'food/item-form.html'

    login_url = '/login/' 

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form, 'item':item})
    
@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id);

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html',{'item':item})
