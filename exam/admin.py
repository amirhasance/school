from django.contrib import admin

from .models import TestModel , Exam , Question , WQuestion , Answer


admin.site.register(TestModel )
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(WQuestion)
admin.site.register(Answer)