# Generated by Django 5.0.2 on 2024-02-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_catagorimodel_taskmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='completaion',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
