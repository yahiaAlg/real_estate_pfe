from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfile(models.Model):
    profile_img=models.ImageField(upload_to=("profiles/%y/%m/%d/"))
    #STATUS_CHOICES= (('GUEST','Guest'), ('PREMIUM','PREMIUM'),('NORMAL','NORMAL'))#comme constant
    
    perferances=models.TextField(blank=True)
    search_history=models.TextField(blank=True)
    background=models.TextField(blank=True)
    owner=models.OneToOneField(User, on_delete=models.CASCADE)
    is_month_seller=models.BooleanField()
    def __str__(self) -> str:
        return f"{self.owner.username}"
    class Status(models.TextChoices):
        GUEST="Guest"
        PREMIUM="PREMIUM"
        NORMAL= "Normal"
    status=models.CharField(max_length=10,choices=Status.choices)
    
class RealtorProfile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)   
    profile_image=models.ImageField(upload_to='realtors/%Y/%m/%d/')
    biographie=models.TextField(blank=True)
    is_seller_of_month=models.BooleanField()
    affiliation_date=models.DateField()
    owner=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:#pour acceder a son nom donner
        return f"{self.owner.username}"
  