from django.contrib import admin

# Register your models here.

from . import models

#  to register we have to type this
admin.site.register(models.Courses)
