from django.db import models
from django.conf import settings


CATERGORY = (
    ('D', "Digital Product"),
    ('P', 'Patner Product')
)

ORDER_STATUS_CHOICES = (
	('created', 'Created'),
	('paid', 'Paid'),
	('shipped', 'Shipped'),
	('refunded', 'Refunded'),
)

ADDRESS_TYPE = (
	('billing', 'Billing'),
	('shipping', 'Shipping'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    title = models.CharField(max_length=150)
    price = models.FloatField()
    category = models.CharField(max_length=2, choices=CATERGORY)
    descrption = models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True)
    quantity = models.IntegerField(default=5, null=True, blank=True)
    slug = models.SlugField()
    discount_price = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=50)
    delivered = models.BooleanField(default=False)
    recieved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	types=models.CharField(max_length = 120, choices = ADDRESS_TYPE)
	street=models.CharField(max_length = 120)
	city=models.CharField(max_length = 120)
	state=models.CharField(max_length = 120)
	zipcode=models.CharField(max_length = 120)

