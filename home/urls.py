from . import views
from django.urls import path

urlpatterns = [
    path('orphanagehome/', views.orphanagehome,name='orphanagehome'),
    path('',views.index,name='index'),
    path('reg/', views.reg,name='reg'),
    path('login/', views.login,name='login'),
    path('donorhome/', views.donorhome,name='donorhome'),
    path('logout/', views.logout, name='logout'),
    path('selectdistrict',views.selectdistrict,name='selectdistrict'),
    path('load-orphanages/', views.load_orphanages, name='ajax_load_orphanages'),
    path('vieworphanage',views.vieworphanage,name='vieworphanage'),
    path('donatehome/', views.donatehome,name='donatehome'),
    path('change_password/',views.change_password,name='change_password'),
    # path('volunteerreg/', views.volunteerreg,name='volunteerreg'),
    path('donate/', views.donate,name='donate'),
    path('profile', views.profile,name='profile'),
    path('address/', views.address,name='address'),
    
    
    # path('add/', views.orphanage_create_view, name='orphanage_add'),
    # path('<int:pk>/', views.orphanage_update_view, name='orphanage_change'),
    
    
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]
