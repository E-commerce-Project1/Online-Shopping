from django.test import TestCase,TransactionTestCase
from blog.models import Post,PostReview,PostOrder,PostOrderItem
from django.contrib.auth.models import User


class TestModelsPostOrder(TestCase):

	def setUp(self):
		test_user3 = User.objects.create_user(username='testuser3', password='1X<ISRUkjhgoiuyh')
		test_user3.save()
		self.postorder1 = PostOrder.objects.create(customer=test_user3,complete=False,transaction_id="some id")

	def testgetcarttotal(self):
		test_user2 = User.objects.create_user(username='testuser2', password='1X<Ikihoiw+tuK')
		test_user2.save()
		test_post1 = Post.objects.create(author=test_user2,price=100,content='content')
		test_post1.save()
		test_postorderitem1 = PostOrderItem.objects.create(post=test_post1,postorder=self.postorder1,quantity=1)
		test_postorderitem1.save()
		self.assertEquals(self.postorder1.get_cart_total,100)		

	def testgetcartitems(self):
		test_user2 = User.objects.create_user(username='testuser2', password='1X<Ikihoiw+tuK')
		test_user2.save()
		test_post1 = Post.objects.create(author=test_user2,price=100,content='content')
		test_post1.save()
		test_postorderitem1 = PostOrderItem.objects.create(post=test_post1,postorder=self.postorder1,quantity=1)
		test_postorderitem1.save()
		self.assertEquals(self.postorder1.get_cart_items,1)	


class TestModelsOrderItem(TestCase):

	def setUp(self):
		test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
		test_user1.save()
		test_user2 = User.objects.create_user(username='testuser2', password='1X<Ikihoiw+tuK')
		test_user2.save()
		test_post1 = Post.objects.create(author=test_user2,price=100,content='content')
		test_post1.save()
		test_postorder1 = PostOrder.objects.create(customer=test_user1,complete=False,transaction_id="some id")
		test_postorder1.save()
		self.postorderitem1 = PostOrderItem.objects.create(post=test_post1,postorder=test_postorder1,quantity=1)		

	def testgettotal(self):
		self.assertEquals(self.postorderitem1.get_total,100)	
