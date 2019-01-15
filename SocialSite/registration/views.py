from django.shortcuts import render

def showLogin(request):
    return render(request,"login.html")



def showSignUp(request):
    return render(request,"signup.html")


