from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from hashlib import sha256
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def orphanagehome(request):
    # request.session.flush()
    return render(request, 'orphanage_index.html')
    
def index(request):
    request.session.flush()
    return render(request, 'index.html')

def reg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        place=request.POST.get('place') 
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        passwords=sha256(pass2.encode()).hexdigest()
        if new_donor.objects.filter(donoremail=email).exists():
            messages.success(request,'Email already Exist....!')
            return redirect('reg')
        else:
            new_donor(donorname=name,donoremail=email,donorphone=phone,donorplace=place,password=passwords).save()
            all_logins(email=email,password=passwords).save()
            print('success')
            messages.success(request,"registered successfully")
            return redirect(login)
    return render(request, 'reg.html')

def login(request):
    request.session.flush()
    if 'email' in request.session:
        return redirect(donorhome)

    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        password2=sha256(password.encode()).hexdigest()
        print(password2)
        donor=all_logins.objects.filter(email=email,password=password2)
        if donor:
            donor_details=all_logins.objects.get(email=email,password=password2)
            email=donor_details.email
            request.session['email']=email
            return redirect('donorhome')
        else:
            print("invalid")
            messages.success(request,"Invalid login Credentials")
            return redirect(login)
    return render(request, 'login.html')

def donorhome(request):
    if 'email' in request.session:
        # id=request.session['id']
        email=request.session['email']
        return render(request, 'donorhome.html',{'id':id,'name':email})
    return redirect(login)

def logout(request):
    if 'email' in request.session:
        request.session.flush()
    return redirect(login)

def selectdistrict(request):
    district= District.objects.all()
    email=request.session['email']
    d = {'district': district,'name':email}
    return render(request,'selectdistrict.html',d)

def load_orphanages(request):
    district_id = request.GET.get('district')
    orphanages = Orphanage.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'orphanage_dropdown_list_options.html', {'orphanages': orphanages})

def vieworphanage(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        district=request.POST.get('district')
        result=Orphanage.objects.filter(id=name,district_id=district)
        print(name,district)
        if result:
            result_details=Orphanage.objects.get(id=name,district_id=district)
            print(result)
            print("orphanage")
            name=result_details.name
            id=result_details.id
            request.session['id']=id
            vieworphanage=Orphanage.objects.all()
            district=District.objects.all()
            email=request.session['email']
            return render(request,'vieworphanage.html',{'name':name,'id':id,'district':district,'vieworphanage':vieworphanage,'name':email})      
        else:
            return redirect(selectdistrict)


    

def donatehome(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        dist=request.POST.get('district')
        item=request.POST.get('item') 
        print(item)
        hname=request.POST.get('hname') 
        city=request.POST.get('city') 
        pin=request.POST.get('pin')
        if 'email' in request.session:
            user=request.session['email']
            print(user)
            donation=userdonate(user_id=user,item_id=item,firstname=fname,lastname=lname,email=email,district_id=dist,phone=phone,city=city,hname=hname,pin=pin)
            donation.save()
            messages.success(request,"Donated successfully")
            return redirect(donate)
    # district=District.objects.all()
    # items=donationtype.objects.all()
    # messages.success(request,"registered successfully")
    # return render(request, 'donatehome.html',{'district':district,'items':items})


def donate(request):
    district=District.objects.all()
    items=donationtype.objects.all()
    email=request.session['email']
    return render(request, 'donatehome.html',{'district':district,'items':items,'name':email})

def profile(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        hname=request.POST.get('hname')
        dist=request.POST.get('district')
        city=request.POST.get('city')
        pin=request.POST.get('pin') 
        if 'email' in request.session:
            user=request.session['email']
            print(user)
            reg = Donorprofile(user_id=user,name=name,phone=phone, hname=hname,district_id=dist,city=city,zipcode=pin)
            reg.save()
            return redirect('address')
    district=District.objects.all()
    email=request.session['email']
    return render(request, 'profile.html',{'district':district,'name':email})

def address(request):
    address=Donorprofile.objects.filter(user=request.session['email'])
    return render(request,'address.html',{'address':address})


def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = all_logins.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'change_password.html')


