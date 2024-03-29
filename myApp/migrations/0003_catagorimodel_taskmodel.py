# Generated by Django 5.0.2 on 2024-02-08 18:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_custom_user_city_alter_custom_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatagoriModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Catagoriy', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('describtion', models.CharField(max_length=100, null=True)),
                ('due_date', models.CharField(max_length=100, null=True)),
                ('completaion', models.CharField(max_length=100, null=True)),
                ('priority', models.CharField(choices=[('high', 'High'), ('mediam', 'Medium'), ('low', 'Low')], max_length=120, null=True)),
                ('Catagoriy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.catagorimodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
