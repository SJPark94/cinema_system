# Generated by Django 2.1.3 on 2018-12-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentSystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='userAccount',
        ),
        migrations.RemoveField(
            model_name='promocode',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='id',
        ),
        migrations.AlterField(
            model_name='promocode',
            name='promotionCode',
            field=models.CharField(blank=True, default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='ticketType',
            field=models.CharField(blank=True, default='', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
