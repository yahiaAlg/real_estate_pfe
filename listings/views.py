from django.shortcuts import render
from listings.models import *
from accounts.models import *
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    total_listings=Listing.objects.all().filter(is_published=True).order_by('-add_date')
    paginator=Paginator(total_listings,6) #Show 
    page = request.GET.get('page',1)
    listings=paginator.get_page(page)
    context={
        "listings":listings
    }
    
    return render(request,'listings/listings.html',context) 
      
def listing(request,listing_id):
    listing=Listing.objects.get(id=listing_id)
    context={
        "page_number":listing_id,
        "listing":listing,
    
    }
    return render(request,'listings/listing.html', context)#Cette ligne de code renvoie une réponse HTTP qui rend un template HTML appelé 'listings/listing.html
