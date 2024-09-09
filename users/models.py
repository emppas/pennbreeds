from django.db import models
from django.contrib.auth.models import User
import calendar
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
        
        # Automatically set the last_payment_date to the last day of the current month if not set
        if not self.last_payment_date:
            self.last_payment_date = self._get_last_day_of_month(now.year, now.month)
        
        # Calculate total_amount_due if last payment date is in a different month than current month
        if self.last_payment_date.month != now.month or self.last_payment_date.year != now.year:
            self.total_amount_due += self.membership_fee_due
            self.last_payment_date = self._get_last_day_of_month(now.year, now.month)
        
        # Update balance_owing based on payment status
        self.balance_owing = self.membership_fee_due if self.payment_status == 'Unpaid' else 0.00
        
        # Calculate overall_debt
        self.overall_debt = self.total_amount_due - self.total_amount_owed

        super().save(*args, **kwargs)

    def _get_last_day_of_month(self, year, month):
        # Get the last day of the month
        last_day = calendar.monthrange(year, month)[1]
        return datetime(year, month, last_day).date()

    def __str__(self):
        return f'{self.user.username} Financial Record'