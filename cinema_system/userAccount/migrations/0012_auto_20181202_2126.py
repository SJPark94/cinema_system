# Generated by Django 2.1.3 on 2018-12-02 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0011_auto_20181202_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentinfo',
            name='userAccount',
        ),
        migrations.DeleteModel(
            name='PaymentInfo',
        ),
    ]