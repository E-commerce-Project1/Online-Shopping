
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('store/', views.store, name="store"),
	path('product/<int:id>/',views.product,name='product'),
	path('productreview/<int:id>/',views.productreview,name='productreview'),
	path('Category/',views.Category,name='Category'),
]
