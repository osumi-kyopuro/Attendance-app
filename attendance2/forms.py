from django import forms
from .models import Attendance
import bootstrap_datepicker_plus as datetimepicker
class AttendForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('user', 'scheduled_attend_time', 'scheduled_leave_time',  'attend_time', 'leave_time',
        'remarks')
        labels = {
            'user': 'スタッフ情報',
            'scheduled_attend_time': '出勤予定時刻',
            'scheduled_leave_time': '退勤予定時刻',
            'attend_time': '出勤時刻',
            'leave_time': '退勤時刻',
            'remarks': '備考欄'
        }
        help_texts = {
            'user': 'スタッフ情報を入力(必須)',
            'scheduled_attend_time': '出勤予定時刻を入力(必須)',
            'scheduled_leave_time': '退勤予定時刻を入力(必須)',
            'attend_time': '出勤時刻を入力(任意)',
            'leave_time': '退勤時刻を入力(任意)',
            'remarks': '備考欄を入力(任意)'
        }
        widgets={
            'scheduled_attend_time': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ),

            'scheduled_leave_time': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ),

            'attend_time': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ),

            'leave_time': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                attrs={'readonly': 'true'},
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                    'ignoreReadonly': True,
                    'allowInputToggle': True,
                }
            ),

        }