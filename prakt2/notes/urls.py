from django.urls import path
from . import views

urlpatterns = [
   path('reg/',views.reg),
   path('reg',views.reg),
   path('login/',views.login_page),
   path('login',views.login_page),
   path('logout/',views.logout_page),
   path('logout',views.logout_page),
   path('notes/',views.notes),
   path('notes',views.notes),
   path('add_notes/',views.add_notes),
   path('add_notes',views.add_notes),
    
]