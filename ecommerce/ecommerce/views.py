from django.shortcuts import render


def home(request):
    context = {
        # from the db fetch user name
        "page_title":"Home Page",
        "user_name":"Kelvin"
    }
    return render(request,"home.html", context)

def about(request):
    
    return render(request,"about.html")