from django.db import models
from django.contrib.auth.models import User
import datetime

import os


def get_file_path(instance, filename):
    original_filename = filename
    now_time = datetime.datetime.now().strftime('%y%m%d%H%M%S')
    filename ="%s%s" %(now_time,original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):  
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.TextField(null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    Product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    Small_description = models.TextField(max_length=250, null=False, blank=False)
    Size = models.TextField(max_length=150,null=True,blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    description2 = models.TextField(max_length=1000, null=True, blank=False)
    Orignal_Price = models.FloatField(null=False, blank=False)
    Selling_Price =models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    Tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.TextField(null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    product_qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Newproducts(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    Product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    Small_description = models.TextField(max_length=250, null=False, blank=False)
    Quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    Orignal_Price = models.FloatField(null=False, blank=False)
    Selling_Price =models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    Tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.TextField(null=False, blank=False)
    meta_description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE ,related_name="Product")    
    image = models.ImageField(upload_to="product")    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)





class Category1(models.Model):  
    slug = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to='path/to/upload', null=True, blank=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class subCategory(models.Model):
    category = models.ForeignKey(Category1, on_delete=models.CASCADE, null=True)  # Temporarily allow null
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to='path/to/upload', null=True, blank=True)
    small_description = models.TextField(max_length=250, null=True, blank=False)
    quantity = models.IntegerField(null=True, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=False)
    original_price = models.FloatField(null=True, blank=False)
    selling_price = models.FloatField(null=True, blank=False)  
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    tag = models.CharField(max_length=150, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Arrival(models.Model):  
    slug = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='path/to/upload', null=True, blank=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    MRP =  models.FloatField(max_length=150,null=True, blank=False)
    SP  =  models.FloatField(max_length=150,null=True,blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Demand(models.Model):  
    slug = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='path/to/upload', null=True, blank=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="Whether the category is hidden or not")
    MRP  =  models.FloatField(null=True,blank=False)    
    SP   =  models.FloatField(null=True,blank=True)
    trending = models.BooleanField(default=False, help_text="Whether the category is trending or not")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Delership(models.Model):
     image = models.ImageField(upload_to='path/to/upload', null=True, blank=True)




class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Name
    

class Feedback(models.Model):
    Name2 = models.CharField(max_length=200)
    Email2 = models.EmailField()
    Phone2 = models.CharField(max_length=200)
    Product2 = models.CharField(max_length=200)
    Message2 = models.TextField()



class Complaint(models.Model):
    Name3 = models.CharField(max_length=200)
    Email3 = models.EmailField()
    Phone3 = models.CharField(max_length=200)
    Product3 = models.CharField(max_length=200)
    Model3 = models.CharField(max_length=200)
    Uploadbill3 = models.ImageField(upload_to=get_file_path, null=True, blank=True)   
    Message3 = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(User ,on_delete= models.CASCADE)
    Fname =models.CharField(max_length=150 ,null=False)
    Lname =models.CharField(max_length=150 ,null=False)
    Email =models.CharField(max_length=150 ,null=False)
    Phone =models.CharField(max_length=150 ,null=False)
    Address =models.TextField(null=False)
    City =models.CharField(max_length=150 ,null=False)
    State =models.CharField(max_length=150 ,null=False)
    Country =models.CharField(max_length=150 ,null=False)
    Pincode =models.CharField(max_length=150 ,null=False)
    Total_price =models.FloatField(max_length=150 ,null=False)
    Payment_mode =models.CharField(max_length=150 ,null=False)
    Payment_Id = models.CharField(max_length= 250 ,null=False)
    orderstatus = (
        ('Pending','Pending'),
        ('Out of Shipping','Out of Shipping'),
        ('Completed','Completed'),

    )

    Status = models.CharField(max_length=190 ,choices=orderstatus , default='Pending')
    message = models.TextField(null=True)
    tracking_no =models.TextField(max_length=150 , null=True)
    Created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return'{}  - {}'.format(self.id, self.tracking_no)
    

class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    Product =models.ForeignKey(Product,on_delete = models.CASCADE)
    Price = models.FloatField(null=False,default=False)
    Quantity =models.IntegerField(null=False, default=False)


    def __str__(self):
         return'{} {}' .format (self.order.id,self.order.tracking_no)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE) 
    phone= models.CharField(max_length=50,null=False)
    address= models.CharField(max_length=50,null=False)
    city= models.CharField(max_length=50,null=False)
    state= models.CharField(max_length=50,null=False)
    country= models.CharField(max_length=50,null=False)
    pincode= models.CharField(max_length=50,null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username