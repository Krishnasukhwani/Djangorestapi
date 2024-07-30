from django.http import HttpResponse

def home(request):
    print("Home page")
    return HttpResponse("This is home page")