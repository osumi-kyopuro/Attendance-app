# Generated by Django 2.2.1 on 2020-11-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20201101_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
