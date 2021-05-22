from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Vanues,History
import smtplib


def dashboard(req):

    vanue=Vanues.objects.all()
    history=History.objects.all()

    return render(req, 'index.html',{'vanue':vanue,'history':history})


def register(req):
    if req.method == "POST":
       
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        uname = req.POST['uname']
        password = req.POST['password']
        repassword = req.POST['repassword']
        
        if User.objects.filter(email=email).exists():
            messages.info(req, 'email already exist !')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.info(req, 'username already exist !')
            return redirect('register')
        else:
            if password != repassword:
                messages.info(req, 'password are not match!')
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save()

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('hardiksavaliya1010@gmail.com', 'Hardik@0794')
                server.sendmail('hardiksavaliya1010@gmail.com', email ,'Hi,' + fname + ' '+ lname + ' your register done')
                server.close()

                return redirect('login')
    else:
        return render(req, 'register.html')


def login(req):

    if req.method == "POST":
        uname = req.POST['uname']
        password = req.POST['password']

        user=auth.authenticate(username=uname,password=password)
        
        if user is not None:
            if user.is_superuser:
                messages.info(req, "Email/Password Invalid!!")
                return redirect('login')
            else:
                auth.login(req,user)
                return redirect('dashboard')
            
        else:
            messages.info(req, "Email/Password Invalid!!")
            return redirect('login')
    else:
        return render(req, 'login.html')


def logout(req):
    auth.logout(req)
    return redirect('dashboard')

def book(req):
    history=History()
    if req.method == "POST":
        history.UserUname = req.POST['loguname']
        history.VanueUname = req.POST['vanuname']
        history.VenueName = req.POST['venue']
        history.Name = req.POST['name']
        history.Email = req.POST['email']
        history.Number = req.POST['number']
        history.Date = req.POST['date']
        history.Time = req.POST['time']
        history.Packege = req.POST['pkg']

        email = req.POST['email']
        name = req.POST['name']
        venueName = req.POST['venue']
        date = req.POST['date']





        # history.Service = req.POST['service[]']

        # service=[]
        # service.append(ser1)
        # service.append(ser2)
        # service.append(ser3)
        # history.Service=service

        history.save()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('hardiksavaliya1010@gmail.com', 'Hardik@0794')
        server.sendmail('hardiksavaliya1010@gmail.com', email ,'Hi,' + name + ' your booking request sent at ' + venueName + ' ')
        server.close()

        messages.info(req, "Booking Request Sent!")
        return redirect('dashboard')
    else:
        return render(req, 'login.html')

def cancel(req):

    if req.method == "POST":
        id = req.POST['cancelid']
        data = req.POST['cancel']

        cancel=History.objects.get(id=id)
        cancel.Status = data
        cancel.save() 

        messages.info(req, "Booking Cancel !")
       
        return redirect('dashboard')
     

    else:
        return HttpResponse("error 404 not found")