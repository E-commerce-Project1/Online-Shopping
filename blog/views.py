from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import *
from .models import Post,PostReview
from blog.forms import PostReviewForm
from django.http import JsonResponse
import json


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=6

class UserPostListView(ListView):
    model=Post
    template_name='blog/user-posts.html'
    context_object_name='posts'
    paginate_by=6

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# class PostCategoryView(ListView):
#    model=Post
#    template_name='blog/category.html'
#    context_object_name='posts'
#    paginate_by=6

#    def get_queryset(self):
#        cat=get_object_or_404(User,category=self.kwargs.get('category'))
#        return Post.objects.filter(category=cat).order_by('-date_posted')


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','price','category','header_image']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
        

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','price','category','header_image']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

        


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})



def updatepostitem(request):

    data = json.loads(request.body)
    postId = data['postId']
    action = data['action']

    print('Action:',action)
    print('productId:', postId)

    customer = request.user
    post = Post.objects.get(id=postId)
    postorder, created = PostOrder.objects.get_or_create(customer=customer,complete = False)
    postorderItem, created = PostOrderItem.objects.get_or_create(postorder=postorder, post=post)

    if action == 'add':
        postorderItem.quantity = (postorderItem.quantity + 1)
    elif action == 'remove':
        postorderItem.quantity = (postorderItem.quantity - 1)

    postorderItem.save()

    if postorderItem.quantity <=  0:
        postorderItem.delete()

    return JsonResponse ('Item was added', safe=False)

