# Generated by Django 2.1.3 on 2018-11-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0009_remove_userinfo_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
