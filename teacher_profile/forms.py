
from django import forms
from klass.models import Tamrin  , File_teacher
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext as _

class Create_Tamrin_Form(forms.ModelForm):
    class Meta:
        model = Tamrin
        fields = ('name' , 'time_expire' , 'file' ,)

    def __init__(self, *args, **kwargs):
        super(Create_Tamrin_Form, self).__init__(*args, **kwargs)
        # self.fields['time_created'] = JalaliDateField(label=_('date time'), # date format is  "yyyy-mm-dd"
        #     widget=AdminJalaliDateWidget # optional, to use default datepicker
        # )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        self.fields['time_expire'] = SplitJalaliDateTimeField(label=_('date time'), 
            widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )

class File_teacher_form(forms.ModelForm):
    class Meta:
        model = File_teacher
        fields = ['name' , 'file' ,]
