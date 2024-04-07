from django.db import models

from django.contrib.auth.models import User
from accounts.models import RealtorProfile,CustomerProfile
# Create your models here.


    
class Listing(models.Model):
    main_image=models.ImageField(upload_to='houses/%Y/%m/%d/')
    slider_image_1=models.ImageField(upload_to='houses/%Y/%m/%d/')
    slider_image_2=models.ImageField(upload_to='houses/%Y/%m/%d/')
    slider_image_3=models.ImageField(upload_to='houses/%Y/%m/%d/')
    slider_image_4=models.ImageField(upload_to='houses/%Y/%m/%d/')
    slider_image_5=models.ImageField(upload_to='houses/%Y/%m/%d/')
    slider_image_6=models.ImageField(upload_to='houses/%Y/%m/%d/')
    description = models.TextField()
    realtor=models.ForeignKey(RealtorProfile, on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey(CustomerProfile, on_delete=models.SET_NULL,null=True)
    # listings_id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garages = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=6, decimal_places=2)
    lot_size = models.DecimalField(max_digits=8, decimal_places=2)
    add_date = models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.title}"
class Annonce(models.Model):
     real_state=models.ForeignKey(Listing, on_delete=models.CASCADE)
     launching_date=models.DateField()
     title=models.TextField(max_length=50)
     content=models.TextField(max_length=100)
     image=models.ImageField()
     promotionel_information=models.TextField(blank=True)
 
    
    
    
# realtor=models.ForeignKey(Realtor,on_delete=models.CASCADE)
 

   
   
   
   
   
   
   
   
       

