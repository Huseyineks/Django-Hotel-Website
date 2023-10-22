from django.shortcuts import render,redirect
from .forms import  Form
from django.views.generic import View
class ContactView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'contact.html')
    


    def post(self,request,*args,**kwargs):
        form = Form(request.POST)
        if form.is_valid():
            newUser = form.save()
            return redirect('homepage')
        return render(request,'contact.html',{'form':form})
