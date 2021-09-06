from django.urls import path
from . import views

app_name='vieapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('sponsor/',views.sponsor,name='sponsor'),
    path('designers/', views.designers, name='designers'),
    path('exhibitor/', views.exhibitor, name='exhibitor'),
    path('model/', views.model, name='model'),
    path('designer/', views.designer, name='designer'),
    path('model/', views.model, name='model'),

]