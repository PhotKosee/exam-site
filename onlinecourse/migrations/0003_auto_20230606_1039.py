# Generated by Django 3.1.3 on 2023-06-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230606_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
