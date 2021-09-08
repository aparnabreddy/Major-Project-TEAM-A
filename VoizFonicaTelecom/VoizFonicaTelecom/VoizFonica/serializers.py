from rest_framework import serializers
from VoizFonica.models import Admin, Queries
from VoizFonica.models import Prepaid
from VoizFonica.models import Postpaid
from VoizFonica.models import Dongle
from VoizFonica.models import Customer
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=("id","adminname","username","password")

class PrepaidSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prepaid
        fields=("id","prename","preamount","prevalidity","prebenefits","preofferdiscount")

class PostpaidSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postpaid
        fields=("id","postname","postamount","postvalidity","postbenefits","postofferdiscount")
        
class DongleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dongle
        fields=("id","planname","dongleamount","donglevalidity","dongleofferdiscount","typeofservices","donglebenefits")

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','cname','address','mobno','email','aadharno','password','profilep','adhaarp')

class QueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Queries
        fields=('id','mobno','queryname','querydes','querysolution')