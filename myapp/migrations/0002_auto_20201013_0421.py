# Generated by Django 2.2.1 on 2020-10-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='authority',
            field=models.IntegerField(null=True),
        ),
    ]