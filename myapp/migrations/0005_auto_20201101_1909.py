# Generated by Django 2.2.1 on 2020-11-01 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201101_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='company_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CustomUser_company_name', to='myapp.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='company_password1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CustomUser_company_password1', to='myapp.Company'),
            preserve_default=False,
        ),
    ]
