# Generated by Django 3.0.4 on 2020-04-16 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
        ('user', '0003_auto_20200401_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(related_name='u_roles', to='role.Role'),
        ),
    ]