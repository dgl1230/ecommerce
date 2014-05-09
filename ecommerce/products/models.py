from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	title = models.CharField(max_length=180)
	description = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
	slug = models.SlugField()
	order = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return str(self.title)

	class Meta:
		ordering = ['-order']

	def get_price(self):
		if self.sale_price > 0:
			return self.sale_price 
		else:
			return self.price 


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to="products/image/")
	title = models.CharField(max_length=120, null=True, blank=True)
	featured_image = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return str(self.title)


class Category(models.Model):
	products = models.ManyToManyField(Product)
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=500)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return str(self.title)

class CategoryImage(models.Model):
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to="products/image/")
	title = models.CharField(max_length=120, null=True, blank=True)
	featured_image = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return str(self.title)