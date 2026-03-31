from django.contrib import admin

from .models import Student, Club, Enrollment

admin.site.register(Student)
admin.site.register(Club)
admin.site.register(Enrollment)
