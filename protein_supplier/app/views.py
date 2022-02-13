from unicodedata import category
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm,MyPasswordChangeForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
#homepage

class ProductView(View):
    def get(self,request):
        totalitem=0
        milk = Product.objects.filter(category='M')
        vegetables = Product.objects.filter(category='V')
        fruits = Product.objects.filter(category='F')
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,'app/home.html',{'milk':milk,'vegetables':vegetables,'fruits':fruits,'totalitem':totalitem})

#productdetailpage   
class product_detailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
           item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
           return render(request,'app/productdetail.html',{'product':product,'item_Already_exists':item_already_in_cart})
        else:
            redirect('accounts/login/')
#addtocartpage
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect(show_cart)    
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        amount=0
        shipping_amount=70.0
        total_amount = 0.0
        cart = Cart.objects.filter(user=user)
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                total_amount = amount + shipping_amount
                return render(request,'app/addtocart.html',{'carts':cart,'total_amount':total_amount,'amount':amount})
        else:
            return render(request,'app/emptycart.html')        
#quantity
def plus_cart(request):
    user = request.user
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                data = {
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':amount + shipping_amount
                }
                return JsonResponse(data)

def minus_cart(request):
    user = request.user
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                data = {
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':amount + shipping_amount
                }
                return JsonResponse(data)

#remove cart
def remove_cart(request):
    user = request.user
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                data = {
                    'amount':amount,
                    'totalamount':amount + shipping_amount
                }
                return JsonResponse(data)





#buynowpage
def buy_now(request):
    return render(request,'app/buynow.html')

#profilepage
@method_decorator(login_required,name="dispatch")
class profileView(View):
    def get(self,request):
        fm = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':fm,'active':'btn btn-primary'})
    def post(self,request):
        fm = CustomerProfileForm(request.POST)
        if fm.is_valid():
            usr = request.user
            name = fm.cleaned_data['name']
            locality=fm.cleaned_data['locality']
            city = fm.cleaned_data['city']
            state=fm.cleaned_data['state']
            zipcode=fm.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'congratulation! profile updated')  
        else:
            messages.error(request,"Sorry! profile can't be updated")    
        return render(request,'app/profile.html',{'form':fm,'active':'btn btn-primary'})      
#address
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',{'address':add,'active':'btn btn-primary'})
#orderspage
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request,'app/orders.html',{'order_placed':op})

#mobilepage
def mobile(request,data=None):
    if data==None:
        mobile = Product.objects.filter(category='M')
    elif (data == 'Sanchi'):
        mobile = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below': 
        mobile = Product.objects.filter(category='M').filter(selling_price__lt=10000)   
    elif data == 'above':
        mobile = Product.objects.filter(category='M').filter(selling_price__gt=10000)    
    return render(request,'app/mobile.html',{'mobiles':mobile})
#vegetablespage
def vegetables(request,data=None):
    if data==None:
        mobile = Product.objects.filter(category='V')
    elif (data == 'Power'):
        mobile = Product.objects.filter(category='V').filter(brand=data)
    elif data == 'below': 
        mobile = Product.objects.filter(category='V').filter(selling_price__lt=10000)   
    elif data == 'above':
        mobile = Product.objects.filter(category='V').filter(selling_price__gt=10000)    
    return render(request,'app/vegetables.html',{'mobiles':mobile})    

#fruitspage
def fruits(request,data=None):
    if data==None:
        mobile = Product.objects.filter(category='F')
    elif (data == 'Power'):
        mobile = Product.objects.filter(category='F').filter(brand=data)
    elif data == 'below': 
        mobile = Product.objects.filter(category='F').filter(selling_price__lt=10000)   
    elif data == 'above':
        mobile = Product.objects.filter(category='F').filter(selling_price__gt=10000)    
    return render(request,'app/fruits.html',{'mobiles':mobile})    
#customerregistrationpage
class customerregistration(View):
    def get(self,request):
        fm = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':fm})
    def post(self,request):
        fm = CustomerRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Congratulation! You have registered successfully')
        else:
            messages.error(request,'Sorry! You have done something wrong ')   
        return render(request,'app/customerregistration.html',{'form':fm})        
#checkoutpage
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    print(add)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        total_amount = amount + shipping_amount    
        return render(request,'app/checkout.html',{'add':add,'totalamount':total_amount,'cart_item':cart_items})

def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect(orders)    
