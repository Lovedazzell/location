from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard.as_view(),name='dash'),
    path('dash/', views.Dashboard.as_view(),name='dash'),
    path('search/', views.Search.as_view(),name='search'),
    path('reference/', views.Reference.as_view(),name='reference'),

    
    path('referance_api/', views.referance_api,name='referance_api'),
    path('search_api/', views.search_api,name='search_api'),
  
]