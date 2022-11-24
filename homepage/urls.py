from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.fetch,name='login'),
    path('register/',views.add,name='register'),
    path('register/success/',views.home,name='success'),
    path('first/',views.login,name='first'),

]
