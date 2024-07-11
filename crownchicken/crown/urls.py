from django.urls import path
from crown import views

urlpatterns = [
   
  
    path('', views.receipt,name='receipt' ),
    path('records',views.records,name='records'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('update/<int:pk>',views.update,name='update'),
    
]