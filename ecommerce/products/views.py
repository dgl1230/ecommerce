from django.shortcuts import render
from django.shortcuts import render, render_to_response, RequestContext, Http404, HttpResponseRedirect,  HttpResponse
from django.template.defaultfilters import slugify
from django.forms.models import modelformset_factory

from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm

from carts.models import Cart



def add_product(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		product = form.save(commit=False)
		product.user = request.user
		product.slug = slugify(form.cleaned_data['title'])
		product.active = False
		product.save()
		return HttpResponseRedirect('/products/%s' %(product.slug))
	return render_to_response("products/edit.html", locals(),
		 context_instance=RequestContext(request))


def edit_product(request, slug):
		instance = Product.objects.get(slug=slug)
		if request.user == instance.user:
			form = ProductForm(request.POST or None, instance=instance)
			if form.is_valid():
				product_edit = form.save(commit=False)
				product_edit.save()
			return render_to_response("products/edit.html", locals(),
		 		context_instance=RequestContext(request))
		else:
			raise Http404


def list_all(request):
	products = Product.objects.filter(active=True)
	return render_to_response("products/all.html", locals(),
		 context_instance=RequestContext(request))



def manage_product_image(request, slug):
	try: 
		product = Product.objects.get(slug=slug)
	except: 
		product = False
	if request.user == product.user:
		queryset = ProductImage.objects.filter(product__slug=slug)
		ProductImageFormset = modelformset_factory(ProductImage, form=ProductImageForm, can_delete=True)
		formset = ProductImageFormset(request.POST or None, request.FILES or None, queryset = queryset)
		form = ProductImageForm(request.POST or None)
		if formset.is_valid():
			for form in formset: 
				instance = form.save(commit=False)
				instance.save()
			if form.deleted_forms:
				formset.save()
		return render_to_response("products/manage_images.html", locals(),
		 	context_instance=RequestContext(request))
	else:
		raise Http404


def single(request, slug):
	product = Product.objects.get(slug=slug)
	images = product.productimage_set.all()
	categories = product.category_set.all()
	edit = True
	try: 
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		for item in cart.cartitem_set.all():
			if item.product == product:
				in_cart = True
	except: 
		in_cart = False
	return render_to_response("products/single.html", locals(),
		 context_instance=RequestContext(request))
