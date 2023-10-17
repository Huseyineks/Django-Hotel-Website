from django.shortcuts import render

def home_page(request):

    return render(request,'home_page.html')
def opportunities(request):
    return render(request,'opportunities.html')

def adult(request):
    return render(request,'adult.html')

def childeren(request):
    return render(request,'childeren.html')

def events(request):
    return render(request,'events.html')
