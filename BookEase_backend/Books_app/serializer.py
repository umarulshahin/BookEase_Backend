from rest_framework import serializers
from .models import *
import re
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = ['id', 'book_title', 'author_name', 'genre', 'book_description', 'book_image', 'created_by']
        read_only_fields = ['created_at', 'updated_at']
        
    
    def validate(self, attrs):
        
        
        base_pattern = r'^(?!\s+$)[A-Za-z][A-Za-z0-9_ ]{2,}$'
        
        if attrs['book_title'] == '' or attrs['author_name'] == '' or attrs['book_description'] == ''  or attrs['genre'] == '' or attrs['created_by'] is None:
            raise serializers.ValidationError({'error' : 'All fields are required'}) 
           
        if self.instance is None and  attrs['book_image'] == '':
                raise serializers.ValidationError({'error' : 'All fields are required'}) 
    
        if not re.match(base_pattern, attrs['book_title']):
            raise serializers.ValidationError({'error':'Invalid Book Name.Book Name must contain atleast 3 characters and must start with a letter'})
        
        if not re.match(base_pattern, attrs['author_name']):
            raise serializers.ValidationError({'error':'Invalid Author Name.Author Name must contain atleast 3 characters and must start with a letter'})
        
        return attrs
    
    def create(self, validated_data): 
        
        book = Books.objects.create(**validated_data)
        book.save()
        return book
    
    def update(self, instance, validated_data):
            
        for fields, value in validated_data.items():
            setattr(instance, fields, value)
            
        instance.save()
        return instance
    
    
class ReadingListSerializer(serializers.ModelSerializer):
    
    book = BookSerializer()
    
    class Meta: 
        model = Reading_List
        fields = ['user','book','position']