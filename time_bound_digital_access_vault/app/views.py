from django.shortcuts import render, redirect
from .models import VaultItems, ShareLinkRules, AuditLogs
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
def main(request):
  return render(request, 'main.html', {})

def view_vault_items(request):
    my_vault_items = VaultItems.objects.all().values()
    return render(request, 'view_vault_items.html', {'my_vault_items':my_vault_items})  

def create_share_link_rules(request):
    my_share_link_rules = ShareLinkRules.objects.all().values()
    return render(request, 'create_share_link_rules.html',{'my_share_link_rules':my_share_link_rules})  

def create_vault_item(request):
   return render(request, 'create_vault_item.html', {})

def login_user(request):
   if request.method=="POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
       login(request, user)
       messages.success(request, ("You Have Been Logged In..."))
       return redirect('main')
    else:
       messages.success(request, ("There was an error, please try again..."))
       return redirect('login')
   else:
    return render(request, 'login.html', {})

def logout_user(request):
   logout(request)
   messages.success(request, ("You have been looged out..."))
   return redirect('main')

def register_user(request):
   return render(request, 'register.html', {})

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You Have Registered Successfully!"))
            return redirect('main')
        else:
           messages.success(request, ("There was a problem registering, please try again."))
        return redirect('register')

    else:
        return render(request, 'register.html', {'form':form})


#    return render(request, 'logout.html', {})

# def audit_logs(request):
#     my_audit_logs = AuditLogs.objects.all().values()
#     template=loader.get_template('audit_logs.html')
#     context={
#         'my_audit_logs':my_audit_logs,
#     }
#     return HttpResponse(template.render(context,request))  



