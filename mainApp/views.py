
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
IsloggedIn=False
LoggedUser=False
class Homepage(APIView):
    # serializer_class = ReactSerializer

    def get (self,request):
        data = {"name":"TANMAY"}
        return Response(data)
    # def homePage (self,request):
    #     data = [{"name":"TANMAY"}]
    #     for detail in React.objects.all()
    #     return Response(data)
    # def signup (self,request):
    #     if request.method == "POST":
    #      name = request.POST.get('name')
    #      email = request.POST.get('email')
    #      password = request.POST.get('password')
    #      branch = request.POST.get('branch')
    #      User = user(name=name, email=email, password=password, branch=branch)
    #      User.save()
    #     return Response({'status':'saved'})
    # def signin (self,request):
    #     data=[]
    #     return Response(details)

class Signin(APIView):
    def post (self,request):
        global IsloggedIn
        
        print(IsloggedIn)
        data={'status':""}
        if IsloggedIn==True :
            data['status']="Already Logged In"
        else :
          if (request.method=="POST"):
            userdata=request.data
            email=userdata['email']
            password=userdata['password']
            User=user.objects.filter(email=email)
            if (len(User)==0):
                data['status']='No User Found'
                IsloggedIn=False
            elif (len(User)==1):
                if (password==User[0].password):
                    data['status']="Success"
                    IsloggedIn=True
                    LoggedUser=User[0]
                else :
                    data['status']='Wrong Email or Password'
                    IsloggedIn=False

            else :
                data['status']='UnIdentified Error'
                IsloggedIn=False

        return Response(data)
class IsSignedIn(APIView):
    def  get(self,request):
        data={'user':"","status":""}
        if IsloggedIn == True and LoggedUser !=False :
            data['status']='LoggedIn'
            data['user']=LoggedUser
        else :
            data['status']='No User LoggedIn'
            data['user']=False 
        return Response(data)
class Signup(APIView):
    def post (self,request):
        if (request.method=="POST"):
            print(IsloggedIn)
            data=request.data
            email=data['email']
            password=data['password']
            name=data['name']
            branch=data['branch']
            User=user(name=name,email=email,password=password,branch=branch)
            User.save()
            data={"Status":"Success"}
        else :
            data:{'Status':"Failed"}
        return Response(data)