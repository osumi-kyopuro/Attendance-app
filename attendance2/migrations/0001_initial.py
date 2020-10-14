# Generated by Django 2.2.1 on 2020-10-10 09:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_attend_time', models.DateTimeField(verbose_name='出勤予定時間')),
                ('scheduled_leave_time', models.DateTimeField(verbose_name='退勤予定時間')),
                ('attend_time', models.DateTimeField(blank=True, null=True, verbose_name='出勤時間')),
                ('leave_time', models.DateTimeField(blank=True, null=True, verbose_name='退勤時間')),
                ('work_time', models.DurationField(default=datetime.timedelta(0), verbose_name='労働時間')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='備考欄')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_schedule', to=settings.AUTH_USER_MODEL, verbose_name='スタッフ情報')),
            ],
        ),
    ]