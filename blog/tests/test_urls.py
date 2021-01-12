from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import home,PostListView,UserPostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,about,main,favorites,postreview,updatepostitem,search
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from users.views import favourite_list,favourite_add

class TestUrls(SimpleTestCase):

	def test_main_url_is_resolved(self):
		url = reverse('main')
		print(resolve(url))
		self.assertEquals(resolve(url).func,main)


	def test_bloghome_url_is_resolved(self):
		url = reverse('blog-home')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,PostListView)


	def test_postreview_url_is_resolved(self):
		url = reverse('postreview', args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,postreview)	


	def test_postdetail_url_is_resolved(self):
		url = reverse('post-detail',args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,PostDetailView)	


	def test_updatepost_url_is_resolved(self):
		url = reverse('update_itempost')
		print(resolve(url))
		self.assertEquals(resolve(url).func,updatepostitem)	

	def test_passwordchange_url_is_resolved(self):
		url = reverse('password_change')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,PasswordChangeView)

	def test_passwordchangedone_url_is_resolved(self):
		url = reverse('password_change_done')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,PasswordChangeDoneView)	

	def test_userpostlist_url_is_resolved(self):
		url = reverse('user-posts',args=['user-username'])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,UserPostListView)	

	def test_postupdate_url_is_resolved(self):
		url = reverse('post-update',args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,PostUpdateView)	
	

	def test_postdelete_url_is_resolved(self):
		url = reverse('post-delete',args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,PostDeleteView)


	def test_postcreate_url_is_resolved(self):
		url = reverse('post-create')
		print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,PostCreateView)	

	def test_about_url_is_resolved(self):
		url = reverse('blog-about')
		print(resolve(url))
		self.assertEquals(resolve(url).func,about)

	def test_favouritelist_url_is_resolved(self):
		url = reverse('favourite_list')
		print(resolve(url))
		self.assertEquals(resolve(url).func,favourite_list)	

	def test_favouriteadd_url_is_resolved(self):
		url = reverse('favourite_add', args=['5'])
		print(resolve(url))
		self.assertEquals(resolve(url).func,favourite_add)	

	def test_search2_url_is_resolved(self):
		url = reverse('search2')
		print(resolve(url))
		self.assertEquals(resolve(url).func,search)			











	

