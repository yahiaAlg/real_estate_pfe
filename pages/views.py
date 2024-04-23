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

from django.db.models import Q
def search(request):
    if request.method == "GET":
        return render(request, 'pages/search.html')
    if request.method == "POST":
        keywords = request.POST.get("keywords","")
        price = request.POST.get("price","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        bedrooms = request.POST.get("bedrooms","")
        transaction_type = request.POST.get("transaction_type", "")
        print("transaction type selected is: ", transaction_type)
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


        # fifth level [lists that contain bedrooms]
        if bedrooms:
            new_search_listings = search_listings.filter(
                bedrooms=bedrooms
            )


        # sixth level [lists that contain price]
        if price:
            new_search_listings = search_listings.filter(
                price__lte=price
            )

        if transaction_type:
            new_search_listings = search_listings.filter(transaction_type=transaction_type)
            pprint(
                new_search_listings
            )

        print("final filter result is:")
        pprint(search_listings)
        context = {
            "listings":search_listings
        }
        return render(request, 'pages/search.html', context)

from accounts.forms import NewUserForm ,Group
def register(request):
    user_form = NewUserForm()

    if request.method == "POST":
        user_form = NewUserForm(request.POST)

        if user_form.is_valid():
            print("info validation processing...")
            new_user = User.objects.create_user(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password1"],
            )
            user_grp = Group.objects.get(name=user_form.cleaned_data["group"])
            new_user.groups.add(user_grp)
            new_user.save()
            print("account created successfully!")
            pprint(user_form.cleaned_data)
            messages.success(request, "account created successfully!")
            return redirect("dashboard")
        else:
            print("error: ", user_form.errors) # type: ignore
            return redirect("register")

    context = {
        "user_form": user_form,
    }
    return render(request, "pages/register.html", context)


def logout(request):
    if request.method == "GET":
        auth.logout(request)
        messages.success(request,"logged out")
        return redirect("home")
    return render(request, 'pages/index.html')


def login(request):
    if request.method == "POST":
        given_username = request.POST.get("username", "")
        given_password = request.POST.get("password", "")
        pprint("user info:")
        pprint(request.POST)
        user_authenticated = User.objects.filter(username=given_username).first()
        print("user password is: ", user_authenticated.password) # type: ignore

        if user_authenticated:
            user_authenticated = auth.authenticate(request, username=given_username, password=given_password)
            if user_authenticated:
                auth.login(request, user_authenticated)
                messages.success(request, "logged in successfully")
                return redirect("home")
            else:
                messages.error(request, "password or username are not correct!")
                return redirect("login")
        else:
            messages.error(
                request, f"no such a user with the name {given_username} in the database!"
            )
    return render(request, "pages/login.html")


from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
def dashboard(request):
    customer=CustomerProfile.objects.filter(owner=request.user).exists()
    if not customer:
        messages.error(request, "Your account needs to be validated by admin first!")
        return redirect("home")
    customer = CustomerProfile.objects.get(owner=request.user)
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
