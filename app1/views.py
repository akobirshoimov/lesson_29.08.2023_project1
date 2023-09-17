from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import SchoolModels,University
from .serializers import Universityserializer,Schoolserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# Create your views here.


# def all_info(request):
#     all = University.objects.all()
#     serializer = Universityserializer(all,many= True)
#     return JsonResponse(serializer.date,safe = False)


# def detail_info(request,univeristy_id):
#     each = get_object_or_404(University,id = univeristy_id)
#     serializer = Universityserializer(University)
#     return JsonResponse(serializer.date)
# class ListSchoolView(APIView):
#     def get(self,request):
#          all = University.objects.all()
#          serializer = Universityserializer(all,many= True)
#          return Response(serializer.data)
class AllView(generics.ListAPIView):
    queryset = SchoolModels.objects.all()
    serializer_class = Schoolserializer
    permission_classes = (IsAuthenticated,)
# class DetailUniversityView(APIView):
#     def get(self,request,*args,**kwargs):
#          each = get_object_or_404(University,id =kwargs ['university_id'] )
#          serializer = Universityserializer(University)
#          return Response(serializer.data)

class CreateView(generics.CreateAPIView):
    queryset = SchoolModels.objects.all()
    serializer_class = Schoolserializer
    permission_classes = (IsAuthenticated,)

class DetailUpdateDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolModels.objects.all()
    serializer_class = Schoolserializer
    permission_classes = (IsAuthenticated,)
    



# class CreateSchoolView(APIView):
#      def post(self,request):
#           data = request.data
#           serializer = Schoolserializer(data = data)
#           if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
               
#           return Response(serializer.errors)
     
    
         
    
    

 


    

