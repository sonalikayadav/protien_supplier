from django.contrib import admin
from .models import Cart,OrderPlaced,Customer,Product
# Register your models here.
#customer model register
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']


#OrderPlaced model register
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

#product model register
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','description','brand','category','product_image']


#orderplaced model register
@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']


