from django.urls import path
from . import views 

urlpatterns = [
    path('',views.list,name='list'),
    path('home/',views.home,name='home'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('create/',views.index,name='index'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('display/<int:id>',views.display,name='display'),
    path('<int:id>/',views.download,name='download'),

]
