from django.shortcuts import render,redirect
from adminapp.models import *
from user.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home1(request):
   
    return render(request,'adminhome.html')
def logout1(request):
    return redirect('userhome')
def categories(request):
    if request.method=="POST":
        image=request.FILES['Image']
        name=request.POST['Categories']
        Admincat.objects.create(
            cat_image=image,
            cat_name=name
        ) 
    return render(request,'categories.html')

def viewcat(request):
    details=Admincat.objects.all()
    context={
        'details':details
    }
    return render (request,'view cat.html',context)

def deletecat(request,deleteid):
    Admincat.objects.filter(id=deleteid).delete()
    return redirect('viewcat')

def add_product(request):
    delta=Admincat.objects.all()
    context={
       'delta':delta 
    }

    if request.method=="POST":
        category_name=request.POST['category']
        pro_image=request.FILES['Prod_Image']
        pro_name=request.POST['product_name']
        brnd_name=request.POST['Brand_Name']
        pro_price=request.POST['Product_Price']
        pro_disc=request.POST['Discount_Details']
        pro_warranty=request.POST['Product_Warranty']
        pro_delivery=request.POST['Delivery Details']
        pro_rate=request.POST['Product_rate']
        
        Products.objects.create(
            Cat_id=Admincat.objects.get(id=category_name),
            product_image=pro_image,
            product_name=pro_name,
            brand_name=brnd_name,
            product_price=pro_price,
            product_disc=pro_disc,
            product_warranty = pro_warranty,
            product_delivery = pro_delivery,
            product_rate=pro_rate,
       
        )
    return render(request,'addproduct.html',context)

def viewprod(request):
    datas=Products.objects.all()
    context={
        'datas':datas
    }
    return render (request,'view_product.html',context)

def edit(request,runid):
    run=Products.objects.filter(id=runid)
    selected_category = Products.objects.get(id=runid).Cat_id
    
    category_details = Admincat.objects.all()
    context={
        'run':run,
        'category_details':category_details,
        'selected_category':selected_category
    }
    return render(request,'edit.html',context)

def update(request,updateid):
    if request.method=='POST':
        try:
            image=request.FILES['Product_Image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file= Products.objects.get(id=updateid).product_image
        cate_name=request.POST['category']    
        pro_name=request.POST['product_name']
        brnd_name=request.POST['Brand_Name']
        pro_price=request.POST['Product_Price']
        pro_disc=request.POST['Discount_Details']
        pro_warranty=request.POST['Product_Warranty']
        pro_delivery=request.POST['Delivery Details']
        pro_rate=request.POST['Product_rate']
        Products.objects.filter(id=updateid).update(
            Cat_id =cate_name,
            product_image=file,
            product_name=pro_name,
            brand_name=brnd_name,
            product_price=pro_price,
            product_disc=pro_disc,
            product_warranty = pro_warranty,
            product_delivery = pro_delivery,
            product_rate=pro_rate,
       
        )
        return redirect('viewprod')
    return render(request,'viewprodut.html')

def deleteprod(request,deleteprodid):
    Products.objects.filter(id=deleteprodid).delete()
    return redirect('viewprod')

def addnotification(request):
    if request.method =='POST':
        title=request.POST['title']
        disc=request.POST['discription']
        Notification.objects.create(
           mess_title= title,
           mess_discription=disc
        )
    return render(request,'addnotification.html')

def viewnotification(request):
    titles= Notification.objects.all()
    context={
       'titles' :titles
    }

    return render(request,'viewnotification.html',context)

def notdelete(request,notdeleteid):
    Notification.objects.filter(id=notdeleteid).delete()
    return redirect('viewnotification')

def viewsign(request):
    shell=Customer.objects.all()
    context={
        'shell' :shell
    }
    return render(request,'viewsign.html',context)

def deletesign(request,signdeleteid):
    Customer.objects.filter(id=signdeleteid).delete()
    return redirect('viewsign')


def complaints(request):
    msg=Contacts.objects.all()
    titles= Notification.objects.all()
    
    context={
        'msg' :msg,
          'titles' :titles
    }
    return render(request,'complaints.html',context)

def delcomplaints(request,delcomplaintsid):
    Contacts.objects.filter(id=delcomplaintsid).delete()
    return redirect('complaints')