from django.test import SimpleTestCase
from django.urls import reverse,resolve
from store.views import store,cart,checkout,updateitem,search,product,productreview,Category
from users.views import favourite_list,favourite_addd



class TestUrls(SimpleTestCase):

	def test_store_url_is_resolved(self):
		url = reverse('store')
		print(resolve(url))
		self.assertEquals(resolve(url).func,store)

	def test_cart_url_is_resolved(self):
		url = reverse('cart')
		print(resolve(url))
		self.assertEquals(resolve(url).func,cart)
		
	def test_checkout_url_is_resolved(self):
		url = reverse('checkout')
		print(resolve(url))
		self.assertEquals(resolve(url).func,checkout)
		
	def test_updateitem_url_is_resolved(self):
		url = reverse('update_item')
		print(resolve(url))
		self.assertEquals(resolve(url).func,updateitem)
		
	def test_search1_url_is_resolved(self):
		url = reverse('search')
		print(resolve(url))
		self.assertEquals(resolve(url).func,search)	

	def test_favouriteaddd_url_is_resolved(self):
		url = reverse('favourite_addd', args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,favourite_addd)
		
	def test_product_url_is_resolved(self):
		url = reverse('product', args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,product)

	def test_favouritelist_url_is_resolved(self):
		url = reverse('favourite_list')
		print(resolve(url))
		self.assertEquals(resolve(url).func,favourite_list)	

	def test_productreview_url_is_resolved(self):
		url = reverse('productreview', args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,productreview)	

	def test_category_url_is_resolved(self):
		url = reverse('Category')
		print(resolve(url))
		self.assertEquals(resolve(url).func,Category)						