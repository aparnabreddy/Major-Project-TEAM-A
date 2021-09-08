from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,response
from django.views.decorators.csrf import csrf_exempt
import json
from VoizFonica.models import Admin, Dongle, Postpaid, Prepaid, Queries
from VoizFonica.serializers import AdminSerializer, QueriesSerializer
from VoizFonica.serializers import PrepaidSerializer
from VoizFonica.serializers import PostpaidSerializer
from VoizFonica.serializers import DongleSerializer
from VoizFonica.models import Customer
from VoizFonica.serializers import CustomerSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

def adminPage(request):
    return render(request,"header1.html")

def loginview(request):
    return render(request,"login.html")

def prepaidview(request):
    return render(request,'addprepaid.html')

def postpaidview(request):
    return render(request,'addpostpaid.html')

def dongleview(request):
    return render(request,'adddongle.html')
    
# def registeradmin(request):
#     return render(request,'register.html')

def previewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/VoizFonica/viewall1/").json
    return render(request,'viewprepaid.html',{"data":fetchdata})

def postviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/VoizFonica/viewall2/").json
    return render(request,'viewpostpaid.html',{"data":fetchdata})

def dongleviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/VoizFonica/viewall3/").json
    return render(request,'viewdongle.html',{"data":fetchdata})

def presearch(request):
    return render(request,'searchprepaid.html')

def postsearch(request):
    return render(request,'searchpostpaid.html')

def donglesearch(request):
    return render(request,'searchdongle.html')
def preupdate(request):
    return render(request,'updateprepaid.html')

def postupdate(request):
    return render(request,'updatepostpaid.html')

def dongleupdate(request):
    return render(request,'updatedongle.html')


def dongledelete(request):
    return render(request,'deletedongle.html')
def prepaiddelete(request):
    return render(request,'deleteprepaid.html')
def postpaiddelete(request):
    return render(request,'deletepostpaid.html')

# @csrf_exempt
# def searchapi(request):
#     try:
#         get=request.POST.get("bno")
#         getbno=Flat.objects.filter(bno=getbuildingno)
#         flat_serializer=FlatSerializer(getbno,many=True)
        
#         return render(request,"search.html",{"data":flat_serializer.data})
#     except Flat.DoesNotExist:
#         return HttpResponse("Invalid building no")
#     except:
#         return HttpResponse("something went wrong")

@csrf_exempt
def addadmin(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        admin_serialize = AdminSerializer(data=mydata)

        if (admin_serialize.is_valid()):
            admin_serialize.save()

            return JsonResponse(admin_serialize.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization", status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get")

@csrf_exempt
def addprepaid(request):
    if (request.method=="POST"):
      

        # mydata=JSONParser().parse(request)
        # prepaid_serialize=PrepaidSerializer(data=mydata)
        prepaid_serialize =PrepaidSerializer(data = request.POST)
        
        if (prepaid_serialize.is_valid()):
            prepaid_serialize.save()
            #return redirect(adminviewss)
            return JsonResponse(prepaid_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def addpostpaid(request):
    if (request.method=="POST"):
        # mydata=JSONParser().parse(request)
        postpaid_serialize=PostpaidSerializer(data=request.POST)
        
        if (postpaid_serialize.is_valid()):
            postpaid_serialize.save()
            #return redirect(adminviewss)
            return JsonResponse(postpaid_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def adddongle(request):
    if (request.method=="POST"):
       

        # mydata=JSONParser().parse(request)
        dongle_serialize=DongleSerializer(data=request.POST)
        
        if (dongle_serialize.is_valid()):
            dongle_serialize.save()
            #return redirect(adminviewss)
            return JsonResponse(dongle_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def admin_all(request):
    if(request.method=="GET"):
        k=Admin.objects.all()
        admin_serializer=AdminSerializer(k,many=True)
        return JsonResponse(admin_serializer.data,safe=False)

@csrf_exempt
def prepaid_all(request):
    if(request.method=="GET"):
        k=Prepaid.objects.all()
        prepaid_serializer=PrepaidSerializer(k,many=True)
        return JsonResponse(prepaid_serializer.data,safe=False)

@csrf_exempt
def postpaid_all(request):
    if(request.method=="GET"):
        k=Postpaid.objects.all()
        postpaid_serializer=PostpaidSerializer(k,many=True)
        return JsonResponse(postpaid_serializer.data,safe=False)

@csrf_exempt
def dongle_all(request):
    if(request.method=="GET"):
        k=Dongle.objects.all()
        dongle_serializer=DongleSerializer(k,many=True)
        return JsonResponse(dongle_serializer.data,safe=False)
# @csrf_exempt
# def f_single(request,fetchid):
    
#     sh=Flat.objects.get(id=fetchid)

    
#     if(request.method=="GET"):
#         flat_serialize=FlatSerializer(sh)
#         return JsonResponse(flat_serialize.data,safe=False,status=status.HTTP_200_OK)
#     if(request.method=="DELETE"):
#         sh.delete()
#         return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
#     if(request.method=="PUT"):
#         mydata=JSONParser().parse(request)
#         flat_serialize=FlatSerializer(sh,data=mydata)

#         if(flat_serialize.is_valid()):
#             flat_serialize.save()
#             return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
#         else:
#             return JsonResponse(flat_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

#########query update#########################################################

@csrf_exempt
def viewquery(request):
    if (request.method=='GET'):
        query=Queries.objects.all()
        queryserial=QueriesSerializer(query,many=True)
        return response.JsonResponse(queryserial.data, safe=False)

def queryview(request):
    fetch=requests.get("http://127.0.0.1:8000/VoizFonica/viewquery/").json()
    return render(request,'viewqueries.html',{"data":fetch})

@csrf_exempt
def updatesearchapiquery(request):
    try:
        getid=request.POST.get("id")
        geti=Prepaid.objects.filter(id=getid)
        q_serializer=QueriesSerializer(geti,many=True)

        return render(request,"updatequery.html",{"data":q_serializer.data})
    except Queries.DoesNotExist:
        return HttpResponse("Invalid query")
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def update_data_readquery(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getmobno=request.POST.get('newmobno')
        getqueryname=request.POST.get('newqueryname')
        getquerydes=request.POST.get('newquerydes')
        getquerysolution=request.POST.get('newquerysolution')
        
        
        mydata={"mobno":getmobno,"queryname":getqueryname,"querydes":getquerydes,"querysolution":getquerysolution}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/VoizFonica/upa/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

def updatequery(request):
    return render(request,'updatequery.html')

@csrf_exempt
def viewquerydetails(request,id):
    
    query=Queries.objects.get(id=id)
    if (request.method=='GET'):
        queryserial=QueriesSerializer(query) 
        return HttpResponse.JsonResponse(queryserial.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=='PUT'):
        mydata=JSONParser().parse(request)
        queryserial=QueriesSerializer(query,data=mydata)
        if (queryserial.is_valid()):
            queryserial.save()
            return HttpResponse.JsonResponse(queryserial.data,status=status.HTTP_200_OK)

########################################################################################




@csrf_exempt
def updatesearchapi1(request):
    try:
        getprename=request.POST.get("prename")
        getpre=Prepaid.objects.filter(prename=getprename)
        prepaid_serializer=PrepaidSerializer(getpre,many=True)

        # return render(request,"update.html",{"data":prepaid_serializer.data})
    except Prepaid.DoesNotExist:
        return HttpResponse("Invalid prename")
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def updatesearchapi2(request):
    try:
        getpostname=request.POST.get("postname")
        getpost=Prepaid.objects.filter(postname=getpostname)
        postpaid_serializer=PostpaidSerializer(getpost,many=True)

        # return render(request,"update.html",{"data":postpaid_serializer.data})
    except Postpaid.DoesNotExist:
        return HttpResponse("Invalid postname")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def updatesearchapi3(request):
    try:
        getdongle=request.POST.get("planname")
        getdo=Dongle.objects.filter(planname=getdongle)
        dongle_serializer=DongleSerializer(getdo,many=True)

        # return render(request,"update.html",{"data":dongle_serializer.data})
    except Dongle.DoesNotExist:
        return HttpResponse("Invalid dongle name")
    except:
        return HttpResponse("something went wrong")
@csrf_exempt
def update_data_read1(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getprename=request.POST.get('newprename')
        getpreamount=request.POST.get('newpreamount')
        getprevalidity=request.POST.get('newprevalidity')
        
        getprebenefits=request.POST.get("newprebenefits")
        getpreofferdiscount=request.POST.get("newpreofferdiscount")
        mydata={"prename":getprename,"preamount":getpreamount,"prevalidity":getprevalidity,"prebenefits":getprebenefits,"preofferdiscount":getpreofferdiscount}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/VoizFonica/view1/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")
@csrf_exempt
def update_data_read3(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getplanname=request.POST.get('newplanname')
        getdongleamount=request.POST.get('newdongleamount')
        getdongleofferdiscount=request.POST.get('newdongleofferdiscount')
        mydata={"planname":getplanname,"dongleamount":getdongleamount,"dongleofferdiscount":getdongleofferdiscount}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/VoizFonica/view3/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")



@csrf_exempt
def update_data_read2(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getpostname=request.POST.get('newpostname')
        getpostamount=request.POST.get('newpostamount')
        getpostvalidity=request.POST.get('newpostvalidity')
        
        getpostbenefits=request.POST.get("newpostbenefits")
        getpostofferdiscount=request.POST.get("newpostofferdiscount")
        mydata={"postname":getpostname,"postamount":getpostamount,"postvalidity":getpostvalidity,"postbenefits":getpostbenefits,"postofferdiscount":getpostofferdiscount}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/VoizFonica/view2/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

@csrf_exempt
def deletesearchapi1(request):
    try:
        getprename=request.POST.get("prename")
        getpre=Prepaid.objects.filter(prename=getprename)
        pre_serializer=PrepaidSerializer(getpre,many=True)
        return render(request,"deleteprepaid.html",{"data":pre_serializer.data})
    except Prepaid.DoesNotExist:
        return HttpResponse("Invalid prename")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def deletesearchapi2(request):
    try:
        getpostname=request.POST.get("postname")
        getpost=Postpaid.objects.filter(postname=getpostname)
        postpaid_serializer=PostpaidSerializer(getpost,many=True)
        return render(request,"deletepostpaid.html",{"data":postpaid_serializer.data})
    except Postpaid.DoesNotExist:
        return HttpResponse("Invalid postname")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def deletesearchapi3(request):
    try:
        getplanname=request.POST.get("planname")
        getplan=Dongle.objects.filter(planname=getplanname)
        dongle_serializer=DongleSerializer(getplan,many=True)
        return render(request,"deletedongle.html",{"data":dongle_serializer.data})
    except Dongle.DoesNotExist:
        return HttpResponse("Invalid Dongle ")
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def delete_data_read1(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/Admins/view1/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")
@csrf_exempt
def delete_data_read2(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/Admins/view2/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")
@csrf_exempt
def delete_data_read3(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        ApiLink="http://localhost:8000/VoizFonica/view3/" +getnewid
        requests.delete(ApiLink)
        return HttpResponse("data has be deleted successfully")

@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getadmin=Admin.objects.filter(username=username,password=password)
    admin_serializer=AdminSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["adminname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'header.html',{"data":admin_serializer.data})
        


    else:
        return HttpResponse("Invalid Credentials")        
            

def customer(request):
    return render(request,'add.html')

def viewplans(request):
    return render(request,'viewplans.html')

def viewCustomers(request):
    fetch = requests.get("http://127.0.0.1:8000/customer/viewall/").json()

    return render(request,'views.html',{"data": fetch})


def updateCustomers(request):
    return render(request,'update.html')

def registersuccess(request):
    return render(request,'cusregistersuccess.html')

@csrf_exempt
def addCustomer(request):
    if(request.method == "POST"):
        # mydict = JSONParser().parse(request)
        c_serializer = CustomerSerializer(data = request.POST)
        if(c_serializer.is_valid()):
            c_serializer.save()
            # return JsonResponse(c_serializer.data,status=status.HTTP_200_OK)
            return redirect(registersuccess)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET method not allowed")

@csrf_exempt
def viewAll(request):
    if(request.method == "GET"):
        user = Customer.objects.all()
        us_serializer = CustomerSerializer(user, many=True)
        return JsonResponse(us_serializer.data, safe=False)

@csrf_exempt
def update_search(request):
    try:
        getCname = request.POST.get("cname")
        getCustomer = Customer.objects.filter(cname = getCname )
        cus_serializer = CustomerSerializer(getCustomer, many=True)
        return render(request,'update.html',{"data":cus_serializer.data}) 
    except:
        return HttpResponse("No Customer found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_data(request):
    getnewid = request.POST.get("newid")
    getcname = request.POST.get("newcname")
    getaddress = request.POST.get("newaddress")
    getmobno = request.POST.get("newmobno")
    getemail = request.POST.get("newemail")
    getaadharno = request.POST.get("newaadharno")
    getpassword = request.POST.get("newpassword")
    
    mydata= {"cname":getcname,"address":getaddress,"mobno":getmobno,"email":getemail,"aadharno":getaadharno,"password":getpassword}
    jsondata = json.dumps(mydata)
    Apilink = "http://127.0.0.1:8000/customer/view/"+getnewid
    requests.put(Apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")  

@csrf_exempt
def login_checkcustomer(request):
    mob=request.POST.get("mobno")
    password=request.POST.get("password")
    getcustomer=Customer.objects.filter(mobno=mob,password=password)
    customer_serializer=CustomerSerializer(getcustomer,many=True)
    if(customer_serializer.data):
        for i in customer_serializer.data:
            x=i["cname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'customerservices.html')
        


    else:
        return HttpResponse("Invalid Credentials")
def loginviewcustomer(request):
    return render(request,"customerlogin.html")     
    
def homepage(request):
    return render(request,"home.html")
def customerservices(request):
    return render(request,'customerservices.html')






################### for query ###############################################################
@csrf_exempt
def addquery(request):
    if(request.method == "POST"):
        # mydict = JSONParser().parse(request)
        c_serializer = QueriesSerializer(data = request.POST)
        if(c_serializer.is_valid()):
            c_serializer.save()
            return JsonResponse(c_serializer.data,status=status.HTTP_200_OK)
            # return redirect(registersuccess)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET method not allowed")

@csrf_exempt
def viewquery(request):
    if(request.method == "GET"):
        query = Queries.objects.all()
        queries_serializer = QueriesSerializer(query, many=True)
        return JsonResponse(queries_serializer.data, safe=False)

@csrf_exempt
def update_search(request):
    try:
        getCname = request.POST.get("cname")
        getCustomer = Customer.objects.filter(cname = getCname )
        cus_serializer = CustomerSerializer(getCustomer, many=True)
        return render(request,'update.html',{"data":cus_serializer.data}) 
    except:
        return HttpResponse("No Customer found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_dataquery(request):
    getnewid = request.POST.get("newid")
    getmobno = request.POST.get("newmobno")
    getqueryname= request.POST.get("newqueryname")
    getquerydes= request.POST.get("newquerydes")
    getquerysolution = request.POST.get("newquerysolution")
    
    mydata= {"mobno":getmobno,"queryname":getqueryname,"querydes":getquerydes,"querysolution":getquerysolution}
    jsondata = json.dumps(mydata)
    Apilink = "http://127.0.0.1:8000/VoizFonica/view/"+getnewid
    requests.put(Apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")  

def cusquery(request):
    return render(request,"Customerquery.html")

def custf(request):
    return render(request,"CustomerFAQ.html")


from django.core.files.storage import FileSystemStorage
def upload(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document']
  
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'add.html')