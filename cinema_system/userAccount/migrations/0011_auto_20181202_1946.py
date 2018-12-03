# Generated by Django 2.1 on 2018-12-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0010_userinfo_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='state',
            field=models.CharField(blank=True, choices=[('', '---'), ('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR')], default='', max_length=2),
        ),
    ]
