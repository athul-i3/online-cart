from django.shortcuts import render,redirect
from adminapp.models import *
from user.models import *
# Create your views here.
def userhome(request):
    war=request.session.get('username')
    card2=Products.objects.all()
    cat=Admincat.objects.all()
    noti=Notification.objects.all()
    user_id=request.session.get('uid')
    num= Cart.objects.filter(userid=user_id).count()
    like=Wishlist.objects.filter(userid=user_id).count()
    subcart= Cart.objects.filter(userid=user_id)
    
    sub_total=0
    for i in subcart:
        sub_total+=i.total

    context={
        'cat': cat,
        'card2': card2,
        'war': war,
        'noti': noti,
        'num': num,
        'like': like,
        'subcart':subcart,
        'sub_total':sub_total
    }
    return render(request,'userhome.html',context)

def shop(request):
    card=Products.objects.all()
    car=Admincat.objects.all()
    noti=Notification.objects.all()
    user_id=request.session.get('uid')
    num= Cart.objects.filter(userid=user_id).count()
    like=Wishlist.objects.filter(userid=user_id).count()
    subcart= Cart.objects.filter(userid=user_id)

    sub_total=0
    for i in subcart:
        sub_total+=i.total

    
    context={
        'card':card,
        'car': car,
        'noti': noti,
        'num': num,
        'like': like,
        'subcart':subcart,
        'sub_total':sub_total
    }
    return render(request,'shop.html',context)



def blog(request):
    return render(request,'blog.html')

def subblog(request):
    return render(request,'subblog.html')

def about(request):
    return render(request,'about.html')


def home2(request):

    return render(request,'home2.html')

def usersign(request):
    if request.method=='POST':
        sign_name=request.POST['username']
        sign_number=request.POST['phone_number']
        sign_email=request.POST['email']    
        sign_password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if sign_password==confirm_password:
            Customer.objects.create(
            username=sign_name,
            phonenumber=sign_number,
            email=sign_email,
            password=sign_password,
            

        )
       
    return render(request,'usersign.html')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if email=="admin123@gmail.com" and password=="123456":
            return redirect('home1')
        elif Customer.objects.filter(email=email,password=password).exists():
            profile=Customer.objects.filter(email=email,password=password).values('username','email', 'id').first()
            request.session['username']=profile['username']
            request.session['email']=profile['email']
            request.session['uid'] = profile['id']
            print(profile)
            return redirect('userhome')    
        else:
            return redirect('sign')
    return render(request,'signin.html')

def contact(request):
    userid=request.session.get('uid')
    user_email=Customer.objects.get(id=userid).email
    noti=Notification.objects.all()
    context={
        'usermail':user_email,
        'noti':noti
    }
    if request.method=='POST':
       
        contact_discription=request.POST['discription']
        Contacts.objects.create(
            cust_id=Customer.objects.get(id=userid),
            discription=contact_discription
            )

    return render(request,'contact.html',context)

def details(request,productid):
    idea=Products.objects.filter(id=productid)
    review=Review.objects.filter(productid=productid)
    userid=request.session.get('uid')
    user1_email=Customer.objects.get(id=userid).email
 
    context={
        'idea':idea,
    'review':review,
      'user1_email':user1_email
    }
    return render(request,'details.html',context)

def cart(request,product2id):
    userid = request.session.get('uid')
    product1_price = Products.objects.get(id=product2id).product_price
    
    if request.method=='POST':
        item_quantity=request.POST['quantity']
        total_price=int(item_quantity) * product1_price

        if not Cart.objects.filter( userid=userid,productid=product2id).exists():
            Cart.objects.create(
                userid = Customer.objects.get(id=userid),
                productid = Products.objects.get(id=product2id),           
                quantity =item_quantity,
                total=total_price
                        
                    )
        else:
                
            Cart.objects.filter( userid=userid,productid=product2id).update(
                quantity =item_quantity,
                total=total_price)

    else:
        if not Cart.objects.filter( userid=userid,productid=product2id).exists():
            Cart.objects.create(
                userid = Customer.objects.get(id=userid),
                productid = Products.objects.get(id=product2id),
                quantity =1,
                total=product1_price
                        
                    )
        else:
                
            Cart.objects.filter( userid=userid,productid=product2id).update(
                quantity =1,
                total=product1_price)



    return redirect('viewcart')

def viewcart(request):
    user_id=request.session.get('uid')
    noti=Notification.objects.all()
    viewcart= Cart.objects.filter(userid=user_id)[::-1]
    num=Cart.objects.filter(userid=user_id).count()
    like=Wishlist.objects.filter(userid=user_id).count()
    subcart= Cart.objects.filter(userid=user_id)

    sub_total=0
    for i in viewcart:
        sub_total+=i.total
     
    context={
        'viewcart':viewcart,
        'noti':noti,
        'sub_total':sub_total,
        'num':num,
        'like':like,
        'subcart':subcart
    }

    return render(request,'features.html',context)

def checkout(request):
    user_id=request.session.get('uid')

    noti=Notification.objects.all()
    viewcart= Cart.objects.filter(userid=user_id)
    user_name=Customer.objects.get(id=user_id).username
    user_phno=Customer.objects.get(id=user_id).phonenumber
    sub_total=0
    for i in viewcart:
        sub_total+=i.total
     
    context={
        'viewcart':viewcart,
        'noti':noti,
        'sub_total':sub_total,
        'user_name':user_name,
        'user_phno':user_phno
    }
 
    if request.method == 'POST':
        add_country=request.POST['country']
        add_state=request.POST['state']
        add_city=request.POST['city']
        add_pincode=request.POST['pincode']
        add_building=request.POST['building_name']
        add_roadname=request.POST['roadname']
        Checkout.objects.create(
            userid=Customer.objects.get(id=user_id),   
            country=add_country,
            state=add_state,
            city=add_city,
            pincode=add_pincode,
            building_name=add_building,
            road_name=add_roadname
            )
        return redirect('checkout')

    return render(request,'checkout.html',context)

def confirm_checkout(request):
    return render(request,'confpay.html')

def review(request,product_id):
    userid=request.session.get('uid')
    if request.method=='POST':
        addreview=request.POST['addreview']
        Review.objects.create(
            userid=Customer.objects.get(id=userid),   
            productid=Products.objects.get(id=product_id),        
            add_review=addreview
        )

        return redirect(f'/details/{product_id}')
    return render(request,'details.html')

def removeitem(request,removeid):
    Cart.objects.filter(id=removeid).delete()
    return redirect('viewcart')

def wishlist(request):
    user_id=request.session.get('uid')
    wishlist=Wishlist.objects.filter(userid=user_id)[::-1]
  
    like=Wishlist.objects.filter(userid=user_id).count()

    num= Cart.objects.filter(userid=user_id).count()
  

    context={
        'wishlist': wishlist,
        'like': like,
        'num': num,
    }
    return render(request,'wishlist.html',context)

def addwishlist(request,productid):
    userid=request.session.get('uid')
    if not Wishlist.objects.filter( userid=userid,productid=productid).exists():
        Wishlist.objects.create(
            userid=Customer.objects.get(id=userid),   
            productid=Products.objects.get(id=productid),                   
        )
    return redirect('wishlist')

def remove_wishlist(request,delete_wishlist):
    Wishlist.objects.filter(id=delete_wishlist).delete()
    return redirect('wishlist')  

def userproduct(request,catid):
    pro=Products.objects.filter(Cat_id=catid)
    subpro=Admincat.objects.all()
    context={
        'pro':pro,
        'subpro':subpro,
    }
    return render(request,'userproduct.html',context)

def userproduct2(request,cat2id):
    pro2=Products.objects.filter(Cat_id=cat2id)
    subpro2=Admincat.objects.all()
    context={
        'pro2':pro2,
        'subpro2':subpro2,
    }
    return render(request,'userproduct2.html',context)

def logout(request):
    del request.session['uid']
    del request.session['email']
    del request.session['username']
    return redirect('signin')

def search(request):
    search_name=request.GET['search']
    if search_name:
        product_search=Products.objects.filter(product_name__icontains=search_name)
        category_search=Admincat.objects.filter(cat_name__icontains=search_name)
        product_by_id=Products.objects.filter(Cat_id__in=category_search)
        item=product_search|product_by_id
        context={
            'item':item
        }
        return render(request,'search.html',context)
    else:
        return redirect('userhome')