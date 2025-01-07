from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    #path('',views.index,name='index'),
    #food/ -index page
    path('',views.IndexClassView.as_view(),name='index'),
    #food/1
    path('item/',views.item,name='item'),
    #path('<int:item_id>/',views.detail, name='detail')
    path('<int:pk>/',views.FoodDetail.as_view(), name='detail'),
    #add
    path('add/',views.create_item,name='create_item'),
    #delete
    path('delete/<int:id>/',views.delete_item, name='delete_item')

]