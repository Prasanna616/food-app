from django.db import models

# Create your models here.

class Item(models.Model):
    #to get object in specific manner use str fun
    def __str__(self):
        #return (self.item_name, self.item_des)
        template = '{0.item_name} {0.item_des}'
        return template.format(self)

    item_name = models.CharField(max_length=200)
    item_des = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://www.google.com/imgres?q=placeholder%20food%20image&imgurl=https%3A%2F%2Fcdn.dribbble.com%2Fusers%2F1012566%2Fscreenshots%2F4187820%2Fmedia%2F985748436085f06bb2bd63686ff491a5.jpg%3Fresize%3D400x0&imgrefurl=https%3A%2F%2Fdribbble.com%2Fwhomohit&docid=6G4983f15vRFnM&tbnid=y4RSZyUgqUsUiM&vet=12ahUKEwj5r5XCwOOIAxWXkq8BHSGXBZ8QM3oFCIABEAA..i&w=400&h=300&hcb=2&ved=2ahUKEwj5r5XCwOOIAxWXkq8BHSGXBZ8QM3oFCIABEAA')
