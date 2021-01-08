from django.urls import path, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,
)
from . import views
urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('update_itempost/', views.updatepostitem, name="update_itempost"),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name='blog-about')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


