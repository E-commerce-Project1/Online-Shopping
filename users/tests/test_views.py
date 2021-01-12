from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

		test_user1.save()
		test_user2.save()


	
	def test_register_GET(self):
		response = self.client.get(reverse('register'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/register.html')



class ProfileTest(TestCase):
	def setUp(self):
		self.client = Client()
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
		test_user1.save()
		test_user2.save()

	def test_redirect_if_not_logged_in(self):
		response = self.client.get(reverse('profile'))
		self.assertRedirects(response, '/login/?next=/profile/') 

	def test_logged_in_uses_correct_template(self):
		login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
		response = self.client.get(reverse('profile'))

		# Check our user is logged in
		self.assertEqual(str(response.context['user']), 'testuser1')
		# Check that we got a response "success"
		self.assertEqual(response.status_code, 200)

		# Check we used correct template
		self.assertTemplateUsed(response, 'users/profile.html')    


class FavouriteListTest(TestCase):
	def setUp(self):
		self.client = Client()
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
		test_user1.save()
		test_user2.save()

	def test_redirect_if_not_logged_in(self):
		response = self.client.get(reverse('favourite_list'))
		self.assertRedirects(response, '/login/?next=/profile/favorites/') 

	def test_logged_in_uses_correct_template(self):
		login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
		response = self.client.get(reverse('favourite_list'))

		# Check our user is logged in
		self.assertEqual(str(response.context['user']), 'testuser1')
		# Check that we got a response "success"
		self.assertEqual(response.status_code, 200)

		# Check we used correct template
		self.assertTemplateUsed(response, 'users/favorites.html')					