from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')

    # Check if user has made inquiry already
    user_id = request.user.id if request.user.is_authenticated else 0
    if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id).exists()
            if has_contacted:
                messages.error(request, 'You have already made an inquiry')
                return redirect('/listings/'+ str(listing_id))
    contact = Contact(
        listing=listing, 
        listing_id=listing_id, 
        name=name, 
        email=email, 
        phone=phone, 
        message=message,
        user_id=user_id,
            )
    contact.save()

    # Send email
    send_mail(
        "Property Listing Inquiry",
        "There is an inquiry for." + listing + '.Sign into admin panel for more info' ,
        "codreanu.d.romeo@gmail.com",
        [realtor_email, "codreanu.danielromeo@yahoo.com"],
         fail_silently=False,
        )

    messages.success(request,'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+ str(listing_id))



