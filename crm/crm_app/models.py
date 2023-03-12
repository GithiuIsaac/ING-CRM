from django.db import models

class Record(models.Model):
    # Automatically add the time at which record is created
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    county = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
