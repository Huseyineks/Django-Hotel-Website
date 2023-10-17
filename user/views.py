from django.shortcuts import render,redirect
from .forms import UserForm

def SupportForm(request):
    form = UserForm(request.POST or None)
    context = dict(
        form = form
    )
    if form.is_valid():
        
        newForm = form.save()
        return redirect('support')
    return render(request,'support.html',context)

