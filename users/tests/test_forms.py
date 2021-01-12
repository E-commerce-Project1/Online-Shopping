from django.test import SimpleTestCase
from users.forms import UserRegisterForm

class TestForms(SimpleTestCase):

	databases = '__all__'

	def test_UserRegisterForm_valid_data(self):
		form = UserRegisterForm(data={'username':'newuser','email':'newuser@company.com','password1':'new000000','password2':'new000000'})
		self.assertTrue(form.is_valid())


	def test_UserRegisterForm_no_data(self):
		form = 	UserRegisterForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors),4)