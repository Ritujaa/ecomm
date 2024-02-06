from django.contrib import admin
from django.urls import path
from beautyapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




urlpatterns = [
     
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('product/<pid>',views.product_details),
    path('about',views.about),
    path('cart',views.cart),
    path('contact',views.contact),
    path('placeorder',views.placeorder),
    path('register',views.register),
    path('login',views.user_login),
    path('forgot',views.forgot_pass),
    path("logout",views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('addtocart/<pid>',views.addtocart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('makepayment',views.makepayment),
#     path('password_reset/', views.password_reset, name='password_reset'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
 ]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
