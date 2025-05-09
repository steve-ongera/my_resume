from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['email']
        m = request.POST['subject']
        a = request.POST['message']
        try:
            Contact.objects.create(name=n, email=g, subject=m, message=a)
            error = "no"
        except:
            error = "yes"
    return render(request,'index.html', locals())



def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def custom_server_error(request):
    return render(request, '500.html', status=500)
