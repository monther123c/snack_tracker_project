from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DateDetailView
from .models import Snack
from django.http import HttpResponse,HttpRequest

# Create your views here.




class SnackListView(ListView):



    template_name = 'snack_list.html'
    model = Snack
    

    def snack_details(request,id):
        
        model=Snack.objects.all()

    
        res_data=render(request,'snack_detail.html',{
            'model':model,
            'path':id
            
            })
        
        return HttpResponse(res_data)