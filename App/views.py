from django.shortcuts import render

def home_page(request):

    return render(request,'home_page.html')

def support(request):
    return render(request,'support.html')

def opportunities(request):
    return render(request,'opportunities.html')

def adult(request):
    return render(request,'events/adult.html')

def childeren(request):
    return render(request,'events/childeren.html')
