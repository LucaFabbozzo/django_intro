from django.urls import path
from . import views

#se esiste questa variabile, django va a concatenare il nome di questa variabile con il nome della rotta
app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name="form"),
    path('<int:product_id>', views.detail, name='detail')
]