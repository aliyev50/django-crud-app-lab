from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=250)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
            # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('book-detail', kwargs={'book_id': self.id})
    
    
class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.book.name}'