from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from .formmodel import MyFormModel
from .models import FormModel

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = MyFormModel(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return redirect()
        else:
            print(form.errors)
    else:
        form= MyFormModel()
    
    context = {
        'form':form
    }
    return render(request,'index.html',context=context)


def dashboard(request):
    users = FormModel.objects.all().values()

    context={
        'dataset':users
    }

    return render(request,'dashboard.html',context=context)