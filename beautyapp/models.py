from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Msg(models.Model):
#     name=models.CharField(max_length=50,verbose_Name=)
#     email=models.CharField(max_length=40)
#     #age=models.IntegerField()
#    # id=models.BigIntegerField()
#     msg=models.CharField(max_length=200)



class Product(models.Model):
    ITEM_FORM_CHOICES = [
          ('All', 'All'),
        ('Gel', 'Gel'),
        ('Cream', 'Cream'),
        ('Lotion', 'Lotion'),
         ('powder', 'powder'),
          ('tablets', 'tablets'),

        # Add more choices as needed
    ]

    SKIN_TYPE_CHOICES = [
        ('All', 'All'),
        ('Oily', 'Oily'),
          ('Dry', 'Dry'),
        ('Combination', 'Combination'),
    ]   # Add more choices as needed

    
    
    CAT=((1,'makeup'),(2,'skincare'),(3,'hair'),(4,'frangrance'),(5,'bath&body'),(6,'health & wellness'))
    name=models.CharField(max_length=40,verbose_name="Product name")
    price=models.FloatField()
    pdetails=models.CharField(max_length=100 ,verbose_name="product_details")
    cat=models.IntegerField(verbose_name="category",choices=CAT)
    is_active=models.BooleanField(default=True,verbose_name="available")
    pimage=models.ImageField(upload_to='image')
    rating = models.FloatField(default=0.0)  
    num_ratings = models.IntegerField(default=0) 
    num_reviews = models.CharField(max_length=100)  
    offers = models.TextField(blank=True, null=True) 
    pdescription=models.TextField(blank=True,null=True)
    item_form = models.CharField(max_length=50, choices=ITEM_FORM_CHOICES,default='Gel')
    skin_type = models.CharField(max_length=50, choices=SKIN_TYPE_CHOICES,default='all')
    brand = models.CharField(max_length=100)
    number_of_items = models.PositiveIntegerField()
    net_quantity = models.CharField(max_length=20)




    def __str__(self):
        return self.name
    


    

class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)
    


class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)


