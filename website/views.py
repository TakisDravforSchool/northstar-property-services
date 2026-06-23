from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import QuoteRequest
# Create your views here.

def home(request):
    return render(request, 'website/home.html')


from django.shortcuts import render, redirect
from .models import QuoteRequest

def home(request):
    if request.method == 'POST':

        quote = QuoteRequest.objects.create(
            full_name=request.POST.get('full_name'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            service_needed=request.POST.get('service_needed'),
            property_type=request.POST.get('property_type'),
            additional_details=request.POST.get('additional_details'),
        )

        send_mail(
            subject='New Quote Request - Northstar Property Services',
            message=f"""
New quote request received.

Name: {quote.full_name}
Phone: {quote.phone_number}
Email: {quote.email}
Address: {quote.address}

Service Needed: {quote.service_needed}
Property Type: {quote.property_type}

Additional Details:
{quote.additional_details}
""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['info@northstarpropertyservices.ca'],
            fail_silently=False,
        )

        return redirect('home')

    return render(request, 'website/home.html')
def services(request):
    return render(request, 'website/services.html')

def about(request):
    return render(request, 'website/about.html')



def gallery(request):
    return render(request, 'website/gallery.html')

def contact(request):
    return render(request, 'website/contact.html')