from django.db import models
from django.contrib.auth.models import User

from products.models import Product



class Cart(models.Model):
	user = models.ForeignKey(User, null=True, blank=True)
	total = models.DecimalField(max_digits=50, default=0, decimal_places=2)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return str(self.id)

class CartItem(models.Model):
	cart = models.ForeignKey(Cart)
	product = models.ForeignKey(Product)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return "%s" %(self.product.title)


