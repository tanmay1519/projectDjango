
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
IsloggedIn=False
LoggedUser=False
loggedUsersdata={}
loggedUsersList=[]
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

# class Signin(APIView):
#     def post (self,request):
#         global IsloggedIn,LoggedUser
        
#         print(IsloggedIn)
#         data={'status':"",'user':{}}
#         if IsloggedIn==True :
#             data['status']="Already Logged In"
#         else :
#           if (request.method=="POST"):
#             userdata=request.data
#             email=userdata['email']
#             password=userdata['password']
#             User=user.objects.filter(email=email)
#             if (len(User)==0):
#                 data['status']='No User Found'
#                 IsloggedIn=False
#             elif (len(User)==1):
#                 if (password==User[0].password):
#                     IsloggedIn=True
#                     LoggedUser={"name":User[0].name,"email":User[0].email,"branch":User[0].branch,"user_id":User[0].user_id}
#                     data['status']="Success"
#                     data['user']=LoggedUser
                    
#                 else :
#                     data['status']='Wrong Email or Password'
#                     IsloggedIn=False

#             else :
#                 data['status']='UnIdentified Error'
#                 IsloggedIn=False

#         return Response(data)
# class IsSignedIn(APIView):
#     def  get(self,request):
#         data={'user':"","status":""}
#         if IsloggedIn == True and LoggedUser !=False :
#             data['status']='LoggedIn'
#             data['user']=LoggedUser
#         else :
#             data['status']='No User LoggedIn'
#             data['user']=False 
#         return Response(data)
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
class AskQuestion(APIView):

    def post(self,request):
      data={'status':""}
     
      if (request.method=="POST"):
        data=request.data
        topic=data['topic']
        Question=data['question']
        user_id=data['user_id']
        Question=question(topic=topic,question=Question,user_id=user_id)
        data['status']="Success"
        Question.save()
      return Response(data)

class LoadQuestions(APIView):
    def get (self,request):
        data={'status':""}
        if (request.method=="GET"):
            questionsList=question.objects.values('question_id','user_id','question','topic','upvote','downvote')
            # change questionList o in a form to transport
            newQuesList=[]
            for oldQues in questionsList:
                tempQues={}
                tempQues['question_id']=oldQues['question_id']
                tempQues['user_id']=oldQues['user_id']
                tempQues['question']=oldQues['question']
                tempQues['downvote']=oldQues['downvote']
                tempQues['upvote']=oldQues['upvote']
                # print("old",(oldQues))
                # print((tempQues))
                newQuesList.append(tempQues)
            for ques in newQuesList :
                ques['answer']=""
                ansList=answer.objects.filter(question_id=ques['question_id'])
                if len(ansList)>0:
                    firstAns=ansList[0]
                    q_id=firstAns.question_id
                    u_id=firstAns.user_id
                    a_id=firstAns.answer_id
                    ans=firstAns.answer
                    upvote=firstAns.upvote
                    downvote=firstAns.downvote
                    selected_answer={'question_id':q_id,'user_id':u_id,'answer_id':a_id,'answer':ans,'upvote':upvote,'downvote':downvote}
                    ques['answer']=selected_answer
                    # sort by upvotes
            print(newQuesList)
            data['status']='Success'
            data['questionsData']=newQuesList
        return Response(data)


# TODO:
class Signin(APIView):
    def post (self,request):
        global loggedUsersdata,loggedUsersList
        data={'status':"",'user':{}}
        userdata=request.data
        email=userdata['email']
        password=userdata['password']
        User=user.objects.filter(email=email)
        # print("CHECK_>>",loggedUsersList,User[0].user_id)
        if len(User) == 0 :
            data['status']='No User Found'
        elif len(User)==1 :
            if User[0].user_id in loggedUsersList:
                data['status']="Already Logged in"
                data['user']=loggedUsersdata[User[0].user_id]
            else :

                if User[0].password == password:
                    LoggedUser={"name":User[0].name,"email":User[0].email,"branch":User[0].branch,"user_id":User[0].user_id}
                    data['status']="Success"
                    data['user']=LoggedUser  
                    loggedUsersList.append(User[0].user_id)
                    loggedUsersdata[User[0].user_id]=LoggedUser
                else :
                    data['status']="Username and Password dont match"
        else :
            data['status']="Unidentified Error" 
        return Response(data)

class IsSignedIn(APIView):
    def post(self,request):
        global loggedUsersdata,loggedUsersList
        dataFromFE=request.data
        data={}
        user_idtocheck=dataFromFE['user_id']
        if user_idtocheck in loggedUsersList :
            data['status']="Success"
            data['user']=loggedUsersdata[user_idtocheck]
        else :
            data['status']="Failure"
        return Response(data)
        # if User[0].user_id in loggedUsersList :
        #     data['status']="Already Logged In"
        # else :
        #   if (request.method=="POST"):
        #     if (len(User)==0):
        #         data['status']='No User Found'
        #         IsloggedIn=False
        #     elif (len(User)==1):
        #         if (password==User[0].password):
        #             IsloggedIn=True
        #             LoggedUser={"name":User[0].name,"email":User[0].email,"branch":User[0].branch,"user_id":User[0].user_id}
        #             data['status']="Success"
        #             data['user']=LoggedUser
                    
        #         else :
        #             data['status']='Wrong Email or Password'
        #             IsloggedIn=False

        #     else :
        #         data['status']='UnIdentified Error'
        #         IsloggedIn=False

        return Response(data)

 
class Signout(APIView):
    
    def post(self,request):
        data={}  
        if request.data :
            user_data=request.data['Signoutuser_id']
            if user_data in loggedUsersList :
               loggedUsersList.remove(user_data)
               loggedUsersdata.pop(user_data)
               data['status']="Success"
            else :  
                data['status']="Failed"
        else :
            data['status']="Failed"
        print(data)
        return Response(data) 
       
class GetUserById(APIView):
    def post(self,request):
        data={}
        which_user = int(request.data['user_id'])
       
        userList = user.objects.filter(user_id=which_user)
     
        if len(userList) == 1 :
            questioner={"user_id":userList[0].user_id,"name":userList[0].name,"email":userList[0].email,"branch":userList[0].branch}
            data['status']="Success"
            data['QuestionUser']=questioner
            
        else :
            data['status']="Failed"
        return Response(data)
class PostAnswer (APIView) :
    def post (self,request):
        data={}
        ans_data=request.data
        Answer = answer(answer=ans_data['answer'],user_id=ans_data['user_id'],question_id=ans_data['question_id'])
        Answer.save()
        data['status']="Success"
        return Response(data)