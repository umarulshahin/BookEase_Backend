from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import *



class BookManagement(APIView):
  
    permission_classes=([IsAuthenticated])
    
    def post(self,request): 
        
        data = request.data
        print(data,'data')
        if not data: 
            return Response('Please provide required fields', status=status.HTTP_400_BAD_REQUEST)
        
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Book Created Successfully'}, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        
        books = Books.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    