from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from beautyapp.models import Product
from beautyapp.models import Cart,Order
from django.db.models import Q
import random
import razorpay




def home(request):
    # # userid=request.user.id
    # # print(userid)
    # print("result:",request.user.is_authenticated)
   
    context={}
    p=Product.objects.filter(is_active=True)
    print(p)
    context['products']=p
    return render(request,'index1.html',context)


def range(request):
    min=request.GET['umin']
    max=request.GET['umax']
   
    print(min)
    print(max)
    q1=Q(price__gte= min)
    q2=Q(price__lte= max)
    q3=Q(is_active=True)
    p=Product.objects.filter(q1 & q2 & q3)
    context={}
    context['products']=p
    return render(request,'index1.html',context)
    # return HttpResponse("value fetch")



def catfilter(request,cv):
    q1=Q(is_active=True)               #prdcut need to be active
    q2=Q(cat=cv)   
    p=Product.objects.filter(q1 & q2)  
    context={}
    context['products']=p
    return render(request,'index1.html',context)
  
  
def sort(request,sv):
    if sv=='0':
        col='price'
    else:
        col='-price'

    p=Product.objects.filter(is_active=True).order_by(col)
    context={}
    context['products']=p
    return render(request,'index1.html',context)

# ###############################################################################################################################

def product_details(request,pid):
    context={}
    context['products']=Product.objects.filter(id=pid)
    return render(request,'product_details.html',context)


# ##################################################################################################################

def addtocart(request,pid):
    if request.user.is_authenticated:
        userid=request.user.id
        u=User.objects.filter(id=userid)
        print(u[0])
        p=Product.objects.filter(id=pid)
        print(p[0])
        c=Cart.objects.create(uid=u[0],pid=p[0])
        c.save()
        return redirect('/cart')
        # print(userid)
        # print(pid)
    
    else:
        return redirect('/login')

# ###################################################################################################################################


def cart(request):
    userid = request.user.id
    c = Cart.objects.filter(uid=userid)
    context = {}
    # if len(c) == 0:
    #     context['errormsg'] = "Cart cannot be empty"
    #     return render(request, 'cart.html', context)
    s = 0
    np = len(c)
    for x in c:
        s += x.pid.price * x.qty
        context['n'] = np
        context['products'] = c
        context['total'] = s
    return render(request, 'cart.html', context)



def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/cart')


def updateqty(request,qv,cid):
    c=Cart.objects.filter(id=cid)
    if qv=='1':
        t=c[0].qty+1
        c.update(qty=t)
    else:
        if c[0].qty>1:
            t=c[0].qty-1
            c.update(qty=t)
    return redirect('/cart')


###########################################################################################################################################
def placeorder(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)
    print("order",oid)
    for x in c:
        # print(x)
        # print(x.pid)
        # print(x.uid)
        # print(x.qty)
        o=Order.objects.create(order_id=oid,pid=x.pid,uid=x.uid,qty=x.qty)
        o.save()
        x.delete()
    orders=Order.objects.filter(uid=request.user.id)
    s=0
    np=len(c)
    for x in c:
        # print(x)
        # print(x.pid.price)
        s=s+x.pid.price * x.qty
        context={}
        context['n']=np
        context['products']=c
        context['total']=s
    return render(request,'placeorder.html',context)



#############################################################################################################################################
def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')



###################################################################################################################################

def user_login(request):
    context={}
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        if uname=="" or upass=="" :
            context['errormsg']="Field cannot be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname, password=upass)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context['errormsg']="Invalid username and password"
                return render(request,'login.html',context)


    else:
        return render(request,'login.html')



def user_logout(request):
    logout(request)
    return redirect('/home')

def register(request):
    context={}
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        upsc=request.POST['upsc']

        if uname=="" or upass=="" or upsc=="":
            context['errormsg']="field cannot be empty"
            return render(request,'register.html',context)
        
        elif upass!=upsc:
            context['errormsg']="password did not match"
            return render(request,'register.html',context)
        
        else:
            try:
                u=User.objects.create(username=uname,password=upass,email=uname)
                u.set_password(upass)
                u.save()
                context['success']="user created succesfully"
                return render(request,'register.html',context)

            except Exception:
                context['errormsg']="username already exist"
                return render(request,'register.html',context)
       
    else:
        return render(request,'register.html')



###########################################################################################################################################


def makepayment(request):
    orders=Order.objects.filter(uid=request.user.id)
    s=0
    for x in orders:
        s=s+x.pid.price*x.qty
        oid=x.order_id
    client = razorpay.Client(auth=("rzp_test_YugNVwM2y3Nf4W", "SZ9fxtfJzVPpyAbUA4f9A8lj"))
    data = { "amount": s*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    print(payment)
    context={}
    
    context['data']=payment
    return render(request,'pay.html',context)




def forgot_pass(request):
    context = {}
    
    if request.method == "POST":
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        upsc = request.POST.get('upsc')
        
        if not uname or not upass or not upsc:
            context['errormsg'] = "All fields are required."
            return render(request, 'forgot_password.html', context)
        
        if upass != upsc:
            context['errormsg'] = "Passwords do not match."
            return render(request, 'forgot_password.html', context)
        
        try:
            user = User.objects.get(username=uname)
        except User.DoesNotExist:
            context['errormsg'] = "User does not exist."
            return render(request, 'forgot_password.html', context)
        
        user.set_password(upass)
        user.save()
        
        context['success'] = "Your password has been successfully reset. Please login with your new password."
        return render(request, 'forgot_password.html', context)
    
    return render(request, 'forgot_password.html')