from django.test import TestCase
from store.models import Product,Order,OrderItem,ShippingAddress,ProductReview
from django.contrib.auth.models import User


class TestModelsOrder(TestCase):

	def setUp(self):
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user1.save()
		self.order1 = Order.objects.create(customer=test_user1,complete=False,transaction_id="some id")

	def testgetcarttotal(self):
		test_product1 = Product.objects.create(name='product 1',price=100,description='new product',brand='any brand')
		test_product1.save()
		test_orderitem1 = OrderItem.objects.create(product=test_product1,order=self.order1,quantity=1)
		test_orderitem1.save()
		self.assertEquals(self.order1.get_cart_total,100)
		
	def testgetcartitems(self):
		test_product1 = Product.objects.create(name='product 1',price=100,description='new product',brand='any brand')
		test_product1.save()
		test_orderitem1 = OrderItem.objects.create(product=test_product1,order=self.order1,quantity=1)
		test_orderitem1.save()
		self.assertEquals(self.order1.get_cart_items,1)	

class TestModelsOrderItem(TestCase):

	def setUp(self):
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user1.save()
		test_product1 = Product.objects.create(name='product 1',price=100,description='new product',brand='any brand')
		test_product1.save()
		test_order1 = Order.objects.create(customer=test_user1,complete=False,transaction_id="some id")
		test_order1.save()
		self.orderitem1 = OrderItem.objects.create(product=test_product1,order=test_order1,quantity=1)		

	def testgettotal(self):
		self.assertEquals(self.orderitem1.get_total,100)	





			


			
