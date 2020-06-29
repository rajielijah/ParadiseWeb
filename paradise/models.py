from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    isActive = model.BooleanField(default=True)

    def __str__(self):
        return self.code


class Product(models.Model):
    title = models.CharField(max_length=150)
    digital = models.BooleanField(default=False)
    descrption = models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True)
    quantity = models.IntegerField(default=5)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    discount_text = models.CharField(max_length=30)
    allow_discount = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title

    @property
    def net_price(self):
        if self.allow_discount:
            return self.discount_price
        else:
            return self.price


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, unique=True)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        if self.coupon:
            if self.coupon.isActive:
                total -= self.coupon.amount
        return total

    def __str__(self):
        return 'Order' + str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.net_price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    country = CountryField(multiple=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Competition_Group(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Competition Group'

    def __str__(self):
        return self.name


class Prize(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.title


class Competition(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField()
    prize_to_win = models.ManyToManyField(Prize)
    belong_to = models.ManyToManyField(
        Competition_Group, related_name='Competitons')
    date_created = models.DateTimeField(auto_now_add=True)
    isFeatured = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    description = models.TextField()
    expiration_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    discount_text = models.CharField(max_length=30)
    allow_discount = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    @ property
    def net_price(self):
        price = self.price
        if self.allow_discount:
            price = self.discount_price
        return price


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    isActive = model.BooleanField(default=True)

    def __str__(self):
        return self.code
