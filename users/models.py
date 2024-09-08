from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from PIL import Image as PILImage
import os

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_approved = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.user.username} Profile'
   
 
class Execo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        # Automatically fill the title and name based on the user's profile
        if self.user and hasattr(self.user, 'profile'):
            self.title = self.user.profile.title
        if self.user:
            self.name = f'{self.user.first_name} {self.user.last_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.position}'
    



class FinancialRecord(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Pending', 'Pending'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_fee_due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount_owed = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    overall_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_payment_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Unpaid')
    balance_owing = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        now = datetime.now().date()
        
        # Automatically fill the last_payment_date with the last day of the month if not set
        if not self.last_payment_date:
            self.last_payment_date = self._get_last_day_of_month()
        
        # Calculate total_amount_due based on monthly membership fee
        if self.last_payment_date.month != now.month:
            self.total_amount_due += self.membership_fee_due
            self.last_payment_date = self._get_last_day_of_month()
        
        # Update balance_owing based on payment status
        self.balance_owing = self.membership_fee_due if self.payment_status == 'Unpaid' else 0.00
        
        # Calculate overall_debt
        if self.total_amount_due > 0 and self.total_amount_owed <= 0:
            self.overall_debt = self.total_amount_due
        else:
            self.overall_debt = self.total_amount_due - self.total_amount_owed

        super().save(*args, **kwargs)

    def _get_last_day_of_month(self):
        first_day_of_next_month = datetime(self.last_payment_date.year, self.last_payment_date.month + 1, 1)
        last_day_of_current_month = first_day_of_next_month - timedelta(days=1)
        return last_day_of_current_month.date()

    def __str__(self):
        return f'{self.user.username} Financial Record'