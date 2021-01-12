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

	def test_store_GET(self):
		response = self.client.get(reverse('store'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'store/store.html')	


	def test_cart_GET(self):
		response = self.client.get(reverse('cart'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'store/cart.html')		

	def test_checkout_GET(self):
		response = self.client.get(reverse('checkout'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'store/checkout.html')

	def test_category_GET(self):
		response = self.client.get(reverse('Category'))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'store/store.html')				

					