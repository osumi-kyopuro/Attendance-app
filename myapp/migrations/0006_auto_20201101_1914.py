# Generated by Django 2.2.1 on 2020-11-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201101_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='company_password1',
            field=models.CharField(max_length=100),
        ),
    ]
