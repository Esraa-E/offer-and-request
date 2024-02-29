from django.shortcuts import render

from .models import *
from .serializers import *

from django.forms.models import BaseModelForm
from django.shortcuts import render , get_object_or_404 , redirect

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from django.views.generic import UpdateView
from django.utils import timezone
from rest_framework.response import Response 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.
#start offer
class offerr(APIView):
    def get(self, request):
        offers = offer.objects.all()
        serializer = offerSerializer(offers, many=True)
        return Response({
            'status':200,'msg':'success',
            'data':serializer.data
             
        })

    def post(self, request):
        serializer = offerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status':200,'msg':'created success',
            'data':serializer.data
             
        })
        return Response({
            'status':400,'msg':'failed created',
            'data':serializer.data,
            'errors':serializer.errors
             
        })
    
  

class offer(APIView): 
     
     def get(self,request,id):
         try:
             offers=offer.objects.get(id=id)
         except offer.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'not found'} )
         serializer=offerSerializer(offers)
        
         return Response({'status':200,'data':serializer.data,'msg':'created success'})

  
 
     def put(self,request,id):
           try:
             offers=offer.objects.get(id=id)
           except offer.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
           serializer= offerSerializer(offers,data=request.data)
          
           if serializer.is_valid():
                 serializer.save()
             
                 return Response({'status':200,'msg':'Updated successfully'} )
          
        
           return Response({'status':404,'errors':serializer.errors,'msg':'Updated failed'} )
          
     def delete(self,request,id):
          try:
             offers=offer.objects.get(id=id)
          except offer.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
        
          offers.delete()
          return Response({'status':200,'msg':'deleted is done'} )



#end offer


# startadd offer
class Addofferr(APIView):
    def get(self, request):
        AddOffers = AddOffer.objects.all()
        serializer = addofferSerializer(AddOffers, many=True)
        return Response({
            'status':200,'msg':'success',
            'data':serializer.data
             
        })

    def post(self, request):
        serializer = addofferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status':200,'msg':'created success',
            'data':serializer.data
             
        })
        return Response({
            'status':400,'msg':'failed created',
            'data':serializer.data,
            'errors':serializer.errors
             
        })
    
  

class Addoffer(APIView): 
     
     def get(self,request,id):
         try:
             AddOffers=AddOffer.objects.get(id=id)
         except AddOffer.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'not found'} )
         serializer=addofferSerializer(AddOffers)
        
         return Response({'status':200,'data':serializer.data,'msg':'created success'})

  
 
     def put(self,request,id):
           try:
             AddOffers=AddOffer.objects.get(id=id)
           except AddOffer.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
           serializer= addofferSerializer(AddOffers,data=request.data)
          
           if serializer.is_valid():
                 serializer.save()
             
                 return Response({'status':200,'msg':'Updated successfully'} )
          
        
           return Response({'status':404,'errors':serializer.errors,'msg':'Updated failed'} )
          
     def delete(self,request,id):
          try:
             AddOffers=AddOffer.objects.get(id=id)
          except AddOffer.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
        
          AddOffers.delete()
          return Response({'status':200,'msg':'deleted is done'} )
    
#end addoffer



# startrequest
class requestt(APIView):
    def get(self, request):
        requestt = request.objects.all()
        serializer = requesrSerializer(requestt, many=True)
        return Response({
            'status':200,'msg':'success',
            'data':serializer.data
             
        })

    def post(self, request):
        serializer = requesrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status':200,'msg':'created success',
            'data':serializer.data
             
        })
        return Response({
            'status':400,'msg':'failed created',
            'data':serializer.data,
            'errors':serializer.errors
             
        })
    
  

class request(APIView): 
     
     def get(self,request,id):
         try:
             requestt=request.objects.get(id=id)
         except request.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'not found'} )
         serializer=requesrSerializer(requestt)
        
         return Response({'status':200,'data':serializer.data,'msg':'created success'})

  
 
     def put(self,request,id):
           try:
             requestt=request.objects.get(id=id)
           except request.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
           serializer= requesrSerializer(requestt,data=request.data)
          
           if serializer.is_valid():
                 serializer.save()
             
                 return Response({'status':200,'msg':'Updated successfully'} )
          
        
           return Response({'status':404,'errors':serializer.errors,'msg':'Updated failed'} )
          
     def delete(self,request,id):
          try:
             requestt=request.objects.get(id=id)
          except request.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
        
          requestt.delete()
          return Response({'status':200,'msg':'deleted is done'} )
#end request


# startcomment
class commentt(APIView):
    def get(self, request):
        commentt = comment.objects.all()
        serializer = commentSerializer(commentt, many=True)
        return Response({
            'status':200,'msg':'success',
            'data':serializer.data
             
        })

    def post(self, request):
        serializer = commentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'status':200,'msg':'created success',
            'data':serializer.data
             
        })
        return Response({
            'status':400,'msg':'failed created',
            'data':serializer.data,
            'errors':serializer.errors
             
        })
    
  

class comment(APIView): 
     
     def get(self,request,id):
         try:
             commentt=comment.objects.get(id=id)
         except comment.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'not found'} )
         serializer=commentSerializer(commentt)
        
         return Response({'status':200,'data':serializer.data,'msg':'created success'})

  
 
     def put(self,request,id):
           try:
             commentt=comment.objects.get(id=id)
           except comment.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
           serializer= commentSerializer(commentt,data=request.data)
          
           if serializer.is_valid():
                 serializer.save()
             
                 return Response({'status':200,'msg':'Updated successfully'} )
          
        
           return Response({'status':404,'errors':serializer.errors,'msg':'Updated failed'} )
          
     def delete(self,request,id):
          try:
             commentt=comment.objects.get(id=id)
          except comment.DoesNotExist:
             return Response({'status':404,'errors':serializer.errors,'msg':'id not found'} )
        
          commentt.delete()
          return Response({'status':200,'msg':'deleted is done'} )
      
    #end comment