from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
	CATEGORIES=(
    ('Bags','Bags'),('Shoes','Shoes'),
    ('Tops','Tops'),('Jeans','Jeans'),
    ('Pants','Pants'),('Mobile Phones','Mobile Phones'),
    ('HeadPhones','HeadPhones')
		)
	category=models.CharField(max_length=100,choices=CATEGORIES,default='none')
	title= models.CharField(max_length=100)
	content= models.TextField()
	header_image=models.ImageField(null=True, blank=True, upload_to="images/",default='/static/blog/product2')
	price=models.CharField(max_length=5)
	date_posted = models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(User,on_delete=models.CASCADE)
	
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk': self.pk})

	def __str__(self):
		return self.title
