from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
#state choices
STATE_CHOICES = (
         ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
         ('Andhra Pradesh','Andhra Pradesh'),
         ('Arunachal Pradesh','Arunachal Pradesh'),
         ('Assam','Assam'),
         ('Bihar','Bihar'),
         ('Chandigarh','Chandigarh'),
         ('Chhattisgarh','Chhattisgarh'),
         ('Dadra Nagar Haveli and Daman Diu','Dadra Nagar Haveli and Daman Diu'),
         ('Goa','Goa'),
         ('Gujarat','Gujarat'),
         ('Haryana','Haryana'),
         ('Himachal Pradesh','Himachal Pradesh'),
         ('Jammu and Kashmir','Jammu and Kashmir'),
         ('Jharkhand','Jharkhand'),
         ('Karnataka','Karnataka'),
         ('Kerala','Kerala'),
         ('Lakshadweep','Lakshadweep'),
         ('Ladakh','Ladakh'),
         ('Madhya Pradesh','Madhya Pradesh'),
         ('Manipur','Manipur'),
         ('Meghalaya','Meghalaya'),
         ('Mizoram','Mizoram'),
         ('Nagaland','Nagaland'),
         ('Delhi','Delhi'),
         ('Odisha','Odisha'),
         ('puducherry','puducherry'),
         ('Punjab','Punjab'),
         ('Rajasthan','Rajasthan'),
         ('Sikkim','Sikkim'),
         ('Tamilnadu','Tamilnadu'),
         ('Telangana','Telangana'),
         ('Tripura','Tripura'),
         ('Uttar Pradesh','Uttar Pradesh'),
         ('Uttrakhand','Uttrakhand'),
         ('West Bengal','West Bengal'),
     )
#customer model
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)
#category model        
CATEGORY_CHOICES=(
    ('M','Milk'),
    ('V','Vegetables'),
    ('F','Fruits'),
)
#product model
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
#cart model
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price     
#status choices
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)
#orderplaced table model
class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    
    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price    
