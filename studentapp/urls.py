from django.urls import path
from studentapp import views

urlpatterns = [
    path('',views.handleindex,name="index"),
    path('insert',views.handleinsert,name="insert"),
    path('update/<id>',views.handleupdate,name="update"),
    path('delete/<id>',views.handledelete,name="delete"),
    
]