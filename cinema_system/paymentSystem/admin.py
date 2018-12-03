from django.contrib import admin
from paymentSystem.models import PromoCode, Tickets, PaymentInfo

# Register your models here.
admin.site.register(PromoCode)
admin.site.register(Tickets)
admin.site.register(PaymentInfo)
