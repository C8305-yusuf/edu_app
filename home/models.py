from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=55)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
