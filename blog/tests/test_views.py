from django.test import TestCase,Client
from django.urls import reverse
from blog.models import Post,PostReview,PostOrder,PostOrderItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		user = User.objects.create(username='user1',password='newuser00')
		user.save()
		testpost = Post.objects.create(title='post1',author=user,category='women',price='100')
		testpost.save()
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

		test_user1.save()
		test_user2.save()


	
	def test_postlist(self):

		response = self.client.get(reverse('blog-home'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/home.html')

	def test_about(self):

		response = self.client.get(reverse('blog-about'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/about.html')
		

	def test_main(self):

		response = self.client.get(reverse('main'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/main.html')	

	

class PostCreateViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
		test_user1.save()
		test_user2.save()

	def test_redirect_if_not_logged_in(self):
		response = self.client.get(reverse('post-create'))
		self.assertRedirects(response, '/login/?next=/post/new/') 

	def test_logged_in_uses_correct_template(self):
		login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
		response = self.client.get(reverse('post-create'))

		# Check our user is logged in
		self.assertEqual(str(response.context['user']), 'testuser1')
		# Check that we got a response "success"
		self.assertEqual(response.status_code, 200)

							
	

			

