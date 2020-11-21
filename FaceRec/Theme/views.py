from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request,"base/base.html")

def change(request,pk):
    
    if pk=="1":
        return render(request,"1/index.html")
    elif pk=="2":
        return render(request,"2/index.html")
    elif pk=="3":
        return render(request,"3/index.html")
