from pprint import pprint
from django.shortcuts import redirect, render
from accounts import*
from .models import *
from listings.models import *
from django.contrib   import messages
# Create your views here.

import smtplib


def send_email(subject, message, receiver_address="yawapen977@acentni.com"):
    # Your email address and password
    sender_address = "meriemmeriem19alg@gmail.com"
    sender_password = "hvds gcfj srsq bmib"



    # Set up the subject and body of the email
    header = f"\r\nSubject: {subject}"
    body = f"\r\n{message}"

    # Combine the headers and the body
    combined = header + body

    # Send the email!
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_address, sender_password)
    server.sendmail(sender_address, receiver_address, combined)
    print("Email sent!")


def contact(request):
    if request.method=="POST":
        listingid=request.POST.get('listing_id',"")


        name=request.POST.get('name',"")
        title=request.POST.get('title',"")
        message=request.POST.get('message',"")
        if listingid and name and title and message:
            customer=CustomerProfile.objects.get(owner=request.user)
            listing=Listing.objects.get(id=listingid)
            contact=Contact(
                real_state=listing,
                customer=customer,
                title=title,
                content=message,
            )
            print("the new contact",contact)
            contact.save()
            send_email(
                f"inquiry about {title} by {customer.owner.username}",
                f"{message}",
                "yawapen977@acentni.com",
            )
            pprint(contact)
            messages.success(request,"contact saved successfuly")
            return redirect("dashboard")
        else:
            messages.error(request,"one of the files is not given")
            return redirect("listing", listingid)


def order(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = Listing.objects.get(id=listing_id)
        #  Check if user has made inquiry already
        if request.user.is_authenticated:

            has_contacted = Order.objects.all().filter(
                listing_id=listing_id, customer=request.user
            )
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this listing"
                )
                return redirect("/listings/" + listing_id)

            else:
                new_order = Order(
                    listing=listing, customer=request.user, email=request.user.email
                )
                new_order.save()
                messages.success(request, "Order saved successfully!")
                return redirect("dashboard")

        messages.success(
            request,
            "Your request has been submitted, a realtor will get back to you soon",
        )
        return redirect("/listings/" + listing_id)
