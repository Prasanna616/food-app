from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    #to get object in specific manner use str fun
    def __str__(self):
        #return (self.item_name, self.item_des)
        template = '{0.item_name} {0.item_des}'
        return template.format(self)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_des = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})