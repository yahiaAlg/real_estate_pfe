from pprint import pprint
from django.shortcuts import render,redirect
from accounts.models import *
from announce.models import Announce
from contact.models import Contact, Order
from listings.models import *
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def index(request):
    first_three=Listing.objects.order_by("-add_date")[:3]

    announcements = Announce.objects.filter(is_published=True).order_by("-add_date")
    context={
        "first_three":first_three,
        "announcements":announcements,
    }
    return render(request, 'pages/index.html',context)
def about(request):
    agent_de_mois=RealtorProfile.objects.get(is_seller_of_month=True)
    agents=RealtorProfile.objects.all()
    context={
        "agent_de_mois":agent_de_mois,
        "agents":agents
            
    }
    return render(request, 'pages/about.html',context)
def search(request):
    if request.method == "GET":
        return render(request, 'pages/search.html')
    if request.method == "POST":
        keywords = request.POST.get("keywords","")
        price = request.POST.get("price","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        bedrooms = request.POST.get("bedrooms","")

        # first level [published lists]
        search_listings = Listing.objects.filter(is_published=True)

        print("searched parmaeters are:")
        pprint(request.POST)

        if keywords:
            new_search_listings = search_listings.filter(
                title__icontains=keywords
            ) 
            search_listings = new_search_listings if new_search_listings.exists() else search_listings
        # second level [lists that contain keywords]

        if keywords:
            new_search_listings = search_listings.filter(description__icontains=keywords)

            search_listings = (
                new_search_listings if new_search_listings.exists() else search_listings
            )
        # third level [lists that contain city]
        if city:
            new_search_listings = search_listings.filter(
                city__icontains=city
            )
            search_listings = new_search_listings if new_search_listings.exists() else search_listings

        # fourth level [lists that contain state]
        if state:
            new_search_listings = search_listings.filter(
                state__icontains=state
            )
            search_listings = (
                new_search_listings if new_search_listings.exists() else search_listings
            )

        # fifth level [lists that contain bedrooms]
        if bedrooms:
            new_search_listings = search_listings.filter(
                bedrooms=bedrooms
            )
            search_listings = (
                new_search_listings if new_search_listings.exists() else search_listings
            )

        # sixth level [lists that contain price]
        if price:
            new_search_listings = search_listings.filter(
                price__lte=price
            )
            search_listings = (
                new_search_listings if new_search_listings.exists() else search_listings
            )

        pprint(search_listings)
        context = {
            "listings":search_listings
        }
        return render(request, 'pages/search.html', context)


def register(request):
    if request.method == "POST":
        username=request.POST.get("username","")
        first_name=request.POST.get("first_name","")
        last_name=request.POST.get("last_name","")
        password1=request.POST.get("password","")
        password2=request.POST.get("password2","")
        email=request.POST.get("email","")
        if User.objects.filter(username=username).exists():
            messages.error(request,"This username is already taken.")
            redirect('register')
        else:
            if email and last_name and first_name: 
                if password1==password2:
                    new_user=User(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1,
                    )
                    new_user.save()
                    messages.success(request, "user created successfully")
                    return redirect('dashboard')
                # WHERE IS THE ELSE OF THIS IF ALSO🥲🥲🥲
                else:
                    messages.error(request, "password didn't match")
                    return redirect('register')
            # WHERE IS THE ELSE OF THIS IF
            else:
                messages.error(request, "one of the fields is empty")
                return redirect('register')

    return render(request, 'pages/registre.html')
def logout(request):
     if request.method == "GET":
        auth.logout(request)
        messages.success(request,"logged out")
        return redirect("home")
     return render(request, 'pages/index.html')
def login(request):
    if request.method=='POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user_authentificated = auth.authenticate(username=username, password=password)
        print('username is: ',user_authentificated)
        if User.objects.filter(username=username).exists():
            if user_authentificated:
                auth.login(request, user_authentificated) 
                return redirect("home")
            else:
                messages.error(request, "password or username are not correct!")
                return redirect("login")
        else:
            messages.error(request, f"no such a user with the name {username} in the database!")
    return render(request, 'pages/login.html')

from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
def dashboard(request):
    customer=CustomerProfile.objects.get(owner=request.user)
    user_contacts = Contact.objects.order_by("-consultation_date").filter(
        customer=customer
    )
    user_orders = Order.objects.order_by("-purchase_date").filter(
        customer=request.user
    )
    pprint(user_contacts)
    context = {
        "contacts": user_contacts,
        "orders": user_orders,
    }
    return render(request, "pages/dashboard.html", context)


def delete_order(request, order_id):

    Order.objects.get(pk=order_id).delete()
    messages.warning(request, f"Order has been deleted!")

    return redirect("dashboard")
