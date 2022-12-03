from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',SnackListView.as_view(),name='snacks_list'),
    path('<int:id>/',SnackListView.snack_details,name='snack_detail_1')
    

]
