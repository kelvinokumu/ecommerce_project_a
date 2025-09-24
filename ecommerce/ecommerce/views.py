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

def shoppinglist(request):
    
    context = {
    "shoppinglist":["Milk", "Eggs", "Butter"]    
    }
    return render(request, "shoppinglist.html",context)


def dashboard(request):
    context = {
        "user_name":"Jane",
        "is_admin":False
    }
    
    return render(request,"dashboard.html", context)