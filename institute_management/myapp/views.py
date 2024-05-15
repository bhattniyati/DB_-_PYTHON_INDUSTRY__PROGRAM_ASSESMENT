from django.shortcuts import render,redirect
from .models import *
import random
from django.contrib import messages
from .utils import *
# from django.contrib.auth import authenticate
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages


# Logic for Home page in Role
def home(request):
    if "email" in request.session:
        user = User.objects.get(email=request.session['email'])
        if user.role == "Principle":
            pid= Principle.objects.get(userid=user)
            context = {
                'user': user,
                'pid': pid
            }
            return render(request, 'home.html', context)
        
        elif user.role=="Student":
            sid= Student.objects.get(userid=user)
            context = {
                'user': user,
                'sid': sid
            }
            return render(request, 'studenthome.html', context)

        else:
            tid= Teacher.objects.get(userid=user)
            context = {
                'user': user,
                'tid': tid
            }
            return render(request, 'teacherhome.html', context)
        
    else:
        return render(request, 'login.html')

# Logic for Student
def student(request):
    user = User.objects.get(email=request.session['email'])
    pid = Principle.objects.get(userid=user)
    context = {
        'user': user,
        'pid': pid,
    }
    return render(request, 'student.html', context)
    
# Logic for Teacher
def teacher(request):
    user = User.objects.get(email=request.session['email'])
    pid = Principle.objects.get(userid=user)
    context = {
        'user': user,
        'pid': pid,
    }
    return render(request, 'teacher.html', context)

# Logic for Login
def login(request):
    if "email" in request.session:
        return redirect("home")
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = User.objects.get(email=email)
                if user.password == password:
                    if user.role=="Principle":
                        request.session['email'] = user.email
                        return redirect("home")
                    elif user.role=="Student":
                        request.session['email'] = user.email
                        return redirect("home")
                    else:
                        request.session['email']=user.email
                        return redirect("home")
                else:
                    messages.error(request, 'Invalid email or password!!')
                    return render(request, "login.html")
            except:
                return render(request, "login.html")
        else:
            return render(request, "login.html")

# Logic for Logout  
def logout(request):
    try:
        del request.session['email']
        del request.session['id']
        return redirect("login")
    except:
        return redirect("login")

# Logic for Add Student
def addstudent(request):
    if "email" in request.session:
        user= User.objects.get(email=request.session['email'])
        pid= Principle.objects.get(userid= user)

        # in this password is passed through mail then student login own profile
        if request.POST:
            email= request.POST['email']
            mobile= request.POST['mobile']
            firstname= request.POST['fname']
            l1= ["123a","123b","123c","123d","124e","124f","124g","124h"]
            password= random.choice(l1) + email[3:6] + mobile[4:7]
            suid= User.objects.create(email= request.POST['email'],password= password,role='Student')

            if suid:
                sid= Student.objects.create( 
                    userid= suid,
                    firstname= request.POST['fname'],
                    lastname= request.POST['lname'],
                    mobile= request.POST['mobile'],
                    birth_date= request.POST['bdate'],
                    roll_no= request.POST['rno'],
                    address= request.POST['add'],
                    fees= request.POST['fees'],
                )

                if sid:
                    mymailfunction("Welcome To Institute Management","mymailtemplate",email,{'firstname':firstname, 'password':password})
                context={
                        'user': user,
                        'pid': pid
                     }
                # messages.success(request,"Student Added Successfully..")
                return render(request, "addstudent.html",context)   
             
        context={
                'user': user,
                'pid': pid,
            }
        return render(request, "addstudent.html",context)  

# Logic for Viewstudent
def viewstudent(request):
    user= User.objects.get(email=request.session['email'])
    pid=Principle.objects.get(userid=user)
    sid= Student.objects.all()
    return render(request,"viewstudent.html",{'sid':sid,'user':user,'pid':pid})

# Logic for perticular student detail
def sdetail(request):
    user= User.objects.get(email=request.session['email'])
    sid= Student.objects.get(userid=user)
    return render(request,"sdetail.html",{'sid':sid,'user':user})

# Logic for perticular teacher detail
def tdetail(request):
    user= User.objects.get(email=request.session['email'])
    tid= Teacher.objects.get(userid=user)
    return render(request,"tdetail.html",{'tid':tid,'user':user})

# Logic for add teacher
def addteacher(request):
    if "email" in request.session:
        user= User.objects.get(email=request.session['email'])
        pid= Principle.objects.get(userid= user)

        # in this password is passed through mail then teacher login own profile
        if request.POST:
            email= request.POST['email']
            firstname= request.POST['fname']
            l1= ["123a","123b","123c","123d","124e","124f","124g","124h"]
            password= random.choice(l1) + email[3:6]
            tuid= User.objects.create(email= request.POST['email'],password= password,role='Teacher')

            if tuid:
                tid= Teacher.objects.create( 
                    userid= tuid,
                    firstname= request.POST['fname'],
                    lastname= request.POST['lname'],
                    mobile= request.POST['mobile'],
                    birth_date= request.POST['bdate'],
                    address= request.POST['add'],
                    salary= request.POST['salary'],
                )

                if tid:
                    mymailfunction("Welcome To Institute Management","mymailtemplate",email,{'firstname':firstname, 'password':password})
                context={
                        'user': user,
                        'pid': pid
                     }
                messages.success(request,"Teacher Added Successfully..")
                return render(request, "home.html",context)   
             
        context={
                'user': user,
                'pid': pid,
            }
        return render(request, "addteacher.html",context)  

# Logic for view teacher
def viewteacher(request):
    user= User.objects.get(email=request.session['email'])
    pid=Principle.objects.get(userid=user)
    tid= Teacher.objects.all()
    return render(request,"viewteacher.html",{'tid':tid,'user':user,'pid':pid})

# Logic for principle profile
def profile(request):
    try:
        if "email" in request.session:
            user= User.objects.get(email=request.session['email'])
            pid=Principle.objects.get(userid=user)

            if request.POST:
                pid.firstname= request.POST['fname']
                pid.lastname= request.POST['lname']
                pid.mobile= request.POST['mobile']
                
                if "picture" in request.FILES:
                    pid.picture= request.FILES['picture']
                    pid.save()
                pid.save() # Update

            context={
                    'user': user,
                    'pid': pid,
                }
            messages.success(request,"Profile Updated Successfully..")
            return render(request, "profile.html",context) 
            
        else:
            return redirect("home")
    except:
        return redirect("home")

# Logic for student profile
def sprofile(request):
    try:
        if "email" in request.session:
            user = User.objects.get(email = request.session['email'])
            sid = Student.objects.get(userid = user)
            
            if request.POST:
                print(sid.userid)
                sid.firstname = request.POST['fname']
                sid.lastname = request.POST['lname']
                sid.mobile = request.POST['mobile']
                sid.address = request.POST['add']
                
                if "picture" in request.FILES:
                    sid.picture = request.FILES['picture']
                    sid.save()

                sid.save()
                
            context={
                'user': user,
                'sid': sid,
            }
            messages.success(request,"Profile Updated Successfully..")
            return render(request, "sprofile.html",context)
        else:
            return redirect("home")
    except:
        return redirect("home")    

# Logic for teacher profile
def tprofile(request):
    try:
        if "email" in request.session:
            user = User.objects.get(email = request.session['email'])
            tid = Teacher.objects.get(userid = user)
            
            if request.POST:
                tid.firstname = request.POST['fname']
                tid.lastname = request.POST['lname']
                tid.mobile = request.POST['mobile']
                tid.address = request.POST['add']
                
                if "picture" in request.FILES:
                    tid.picture = request.FILES['picture']
                    tid.save()

                tid.save()
                
            context={
                'user': user,
                'tid': tid,
            }
            messages.success(request,"Profile Updated Successfully..")
            return render(request, "tprofile.html",context)
        else:
            return redirect("home")
    except:
        return redirect("home")    
    
# Logic for changepassword for all
def changepassword(request):
    try:
        user= User.objects.get(email=request.session['email'])
        pid = Principle.objects.filter(userid=user).first() # first object return 
        sid = Student.objects.filter(userid=user).first()
        tid = Teacher.objects.filter(userid=user).first()
        
        if request.method=="POST":
            if user.password==request.POST['cpassword']:
                if request.POST['npassword']==request.POST['cnewpassword']:
                    user.password=request.POST['npassword']
                    user.save()
                    return redirect("logout")
                
                else:
                    messages.error(request,"New Password and Confrim Password doest not match !!")
                    if user.role=="Principle":
                        return render(request,"changepassword.html",{'pid':pid,'user':user})
                    elif user.role=="Student":
                            return render(request,"scpassword.html",{'sid':sid,'user':user})
                    else:
                        return render(request,"tcpassword.html",{'tid':tid,'user':user})
                    

            else:
                messages.error(request,"Old Password does not match !!")
                if user.role=="Principle":
                        return render(request,"changepassword.html",{'pid':pid,'user':user})
                elif user.role=="Student":
                        return render(request,"scpassword.html",{'sid':sid,'user':user})
                else:
                    return render(request,"tcpassword.html",{'tid':tid,'user':user})
                
        else:
            if user.role=="Principle":
                return render(request,"changepassword.html",{'pid':pid,'user':user})
            elif user.role=="Student":
                    return render(request,"scpassword.html",{'sid':sid,'user':user})
            else:
                return render(request,"tcpassword.html",{'tid':tid,'user':user})
    
    except:
        return redirect("home")

# Logic for forgot password using email through
def fpassword_email(request):
    if request.method=="POST":
            email= request.POST['email']
            request.session['email']=request.POST['email']
            
            passw= random.randint(100001,999999)
            request.session['passw']=passw
            mymailfunction("Welcome to Myapp","mymailtemplate2",email,{'email':email,"passw":passw})
            return render(request,"password.html")
          
    else:
        return render(request,"fpassword_email.html")

def password(request):
     if request.method=="POST":
        password= int(request.session['passw'])
        upassword= int(request.POST['password'])

        if password==upassword:
            del request.session['passw']
            return render(request,"email_newpassword.html") 

        else:
            messages.error(request,"Invalid Password !")     
            return render(request, "email_newpassword.html") 
        
     else:
        return render(request,"password.html")
     
def email_newpassword(request):
    if request.method=="POST":
            user= User.objects.get(email=request.session['email'])

            if request.POST['e_newpassword']==request.POST['e_cpassword']:
                user.password=request.POST['e_newpassword']
                user.save()
                return render(request,"login.html")
            
            else:
                messages.error(request,"New Password and Confirm Password does not match !!")
                return render(request,"email_newpassword.html")
        
    else:
        return render(request,"email_newpassword.html")