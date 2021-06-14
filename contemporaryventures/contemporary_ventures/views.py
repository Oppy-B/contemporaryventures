
# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.conf import settings
from blog.models import Post

import os




#class IndexView(ListView):
#    template_name = "contemporary_ventures/about.html"

def cv_index(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/index.html", context)

def about_us(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/about_2.html", context)

def contact(request):
    email_from = settings.EMAIL_HOST_USER
    form = ContactForm()
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']
            your_phone = form.cleaned_data['your_phone']
            message = form.cleaned_data['message']
            all_message = (f'NAME : {your_name} \nEMAIL : {your_email} \nMESSAGE : {message}')

            '''
            message = Mail(
            from_email='from_email@example.com',
            to_emails='to@example.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>')

            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

            '''
            send_mail('Finally, it worked',all_message, email_from, ['bisiriyuopeyemi14@gmail.com'],fail_silently=False)
    form = ContactForm()

    context = {
        'form':form,
        'first_3_post':first_3_post
    }
    return render(request, "contemporary_ventures/contact_3.html", context )

def handler404(request, exception):
    context = {}
    return render(request, "contemporary_ventures/404.html", context=context)

def handler505(request, exception):
    context = {}
    return render(request, "contemporary_ventures/505.html", context=context)


def custom_page_not_found_view(request, exception):
    return render(request, "contemporary_ventures/404.html")

def proj_apartment_cleaning(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/project_apartment_cleaning.html", context)

def project(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/projects.html",context)

def project_after_renovation_cleaning(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/project_after_renovation_cleaning.html", context)

def service_house_cleaning(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/service_house_cleaning.html", context)

def services(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/services.html", context)

def service_post_renovation(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/service_post_renovation.html", context)

def service_window_cleaning(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/service_window_cleaning.html", context)

def service_commercial_cleaning(request):
    first_3_post = Post.objects.all().order_by('-created_on')[:3]
    context = {
        'first_3_post' : first_3_post
    }
    return render(request, "contemporary_ventures/service_commercial_cleaning.html", context)