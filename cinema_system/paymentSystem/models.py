from django.db import models
from userAccount.models import UserInfo

# Create your models here.

class PaymentInfo(models.Model):

    userAccount = models.OneToOneField(UserInfo,
                                       on_delete=models.CASCADE,
                                       primary_key=True)

    cardNumber = models.CharField(max_length=50, blank=True, default='0000')
    cardMonth = models.CharField(max_length=50, blank=True, default='0000')
    cardYear = models.CharField(max_length=50, blank=True, default='0000')
    cardPin = models.CharField(max_length=50, blank=True, default='0000')
    cardFirstName = models.CharField(max_length=50, blank=True, default='')
    cardLastName = models.CharField(max_length=50, blank=True, default='')

class PromoCode(models.Model):

    promotionCode = models.CharField(max_length=50, blank=True, default='', primary_key=True)
    discountPercentage = models.CharField(max_length=25, blank=True, default='00')

class Tickets(models.Model):

    ticketType = models.CharField(max_length=50, blank=True, default='', primary_key=True)
    ticketPrice = models.CharField(max_length=20, blank=True, default='00')

