from django.db import models
from Authentication_app.models import CustomUser
# Create your models here.

class Books(models.Model): 
    
    GENRE_CHOICES = [
    ('fiction', 'Fiction'),
    ('non_fiction', 'Non-Fiction'),
    ('romance', 'Romance'),
    ('fantasy', 'Fantasy'),
    ('mystery', 'Mystery'),
    ('thriller', 'Thriller'),
    ('science_fiction', 'Science Fiction'),
    ('historical', 'Historical'),
    ('biography', 'Biography'),
    ('self_help', 'Self Help'),
    ('horror', 'Horror'),
    ('poetry', 'Poetry'),
    ('adventure', 'Adventure'),
    ('young_adult', 'Young Adult'),
    ('children', 'Children'),
    ('drama', 'Drama'),
    ]

    
    book_title = models.CharField(max_length=100, blank=False)
    author_name = models.CharField(max_length=100, blank=False)
    book_description = models.TextField(blank=False)
    book_image = models.ImageField(upload_to='books/', max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, blank=False)
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='created_by', blank=False)
    
    class Meta:
        ordering = ['-created_at']
        
class Reading_List(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, blank=False)
    position = models.IntegerField(blank=False,default=0)
    
    
    
    class Meta: 
        ordering = ['-position']
        unique_together = ('user','book')