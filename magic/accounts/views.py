from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView,View,FormView
from django.contrib.auth.mixins import LoginRequiredMixin






# @login_required
# def profile(request):
#     ...

# class login(View):
#     template_name = "accounts/login.html"
#     def get(self,request):
#         render(request, self.template_name)
class Dashboard(LoginRequiredMixin,View):

    template_name = "registration/dashboard.html"
    def get(self,request):
        return render(request, self.template_name)

class Register(View):
    template_name = "registration/register.html"
    def get(self,request):
        form = UserCreationForm()
        return render(request, self.template_name, {
            "form": form
        })
    def post(self, request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)

            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("dashboard")
        else:
            form = UserCreationForm()

        return render(request, self.template_name, {
            "form": form
        })
    
# class Logout(View):
#     def get(self,request):
#         redirect("search")