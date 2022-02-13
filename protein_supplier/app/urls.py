from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('',views.ProductView.as_view()),
    path('product-detail/<int:pk>',views.product_detailView.as_view(),name="product-detail"),
    path('cart/',views.add_to_cart,name='add-to-cart'),
    path('show_cart/',views.show_cart,name="show_cart"),
    path('pluscart/',views.plus_cart,name="plus_cart"),
    path('minuscart/',views.minus_cart,name="minus_cart"),
    path('removecart/',views.remove_cart,name='remove_cart'),
    path('buy/',views.buy_now,name="buy-now"),
    path('profile/',views.profileView.as_view(),name='profile'),
    path('address',views.address,name='address'),
    path('orders/',views.orders,name='orders'),
    path('changepassword/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/changepassworddone/'),name='changepassword'),
    path('changepassworddone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/changepassworddone.html'),name="changepassworddone"),
    path('passwordreset/',auth_view.PasswordResetView.as_view(template_name="app/passwordreset.html",form_class=MyPasswordResetForm,success_url='/passwordresetdone/'),name="passwordreset"),
    path('passwordresetdone/',auth_view.PasswordResetDoneView.as_view(template_name="app/passwordresetdone.html"),name="password_reset_done"),
    path('passwordresetconfirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name="app/passwordresetconfirm.html",form_class=MySetPasswordForm),name="password_reset_confirm"),
    path('passwordresetcomplete/',auth_view.PasswordResetCompleteView.as_view(template_name="app/passwordresetcomplete.html"),name="password_reset_complete"),
    path('mobile/',views.mobile,name='mobile'),
    path('mobile/<slug:data>',views.mobile,name='mobiledata'),
    path('vegetables/',views.vegetables,name='vegetables'),
    path('fruits/',views.fruits,name='fruits'),
    path('fruits/<slug:data>',views.fruits,name='fruitsdata'),
    path('vegetables/<slug:data>',views.vegetables,name='vegetablesdata'),
    path('registration/',views.customerregistration.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name="logout"),
    path('checkout/',views.checkout,name='checkout'),
    path('paymentdone/',views.payment_done,name="paymentdone"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

