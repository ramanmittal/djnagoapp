from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method=="POST":
        realtor_email=request.POST.get("realtor_email")
        listing_id=request.POST.get("listing_id")
        listing=request.POST.get("listing")
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        user_id=None
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id ,user_id=user_id)
            if has_contacted:
                messages.error(request,"all ready make an inquiry")
                return redirect("/listings/"+listing_id)
        contact=Contact(listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,message=message,user_id=user_id) 
        contact.save()
        send_mail('Listing Inquiry','For'+listing,'from@example.com',[email],fail_silently=False,)
        messages.success(request,"Your request has been submitted.")
        return redirect("/listings/"+listing_id)

    pass
