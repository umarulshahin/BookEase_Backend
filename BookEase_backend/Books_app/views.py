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
        if not data: 
            return Response('Please provide required fields', status=status.HTTP_400_BAD_REQUEST)
        
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Book Created Successfully','data' : serializer.data}, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        
        books = Books.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request): 
        
        id = request.data.get('id')
        user_id = request.data.get('user_id')
        
        if not id or not user_id:
            return Response('please provide required fields', status=status.HTTP_400_BAD_REQUEST)
        
        try:
            
            book = Books.objects.get(id=id,created_by = user_id)
            book.delete()
            return Response('Book Deleted Successfully', status=status.HTTP_200_OK)
        
        except Books.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request):
        
        data = request.data
        
        if not data or not id:
            return Response('Please provide required fields', status=status.HTTP_400_BAD_REQUEST)
        
        try:
            
            book = Books.objects.get(id=data['id'])
            
            serializer = BookSerializer(book, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Book Updated Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Books.DoesNotExist:
            return Response('Book not found', status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e: 
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)