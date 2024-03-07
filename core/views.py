from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def _(request):
    return render(request, 'core/class.html')

def contact(request):
    return render(request, 'core/contact.html')

def single(request):
    return render(request, 'core/single-class.html')

def message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        classes = request.POST['class']
        message = request.POST['message']

        
