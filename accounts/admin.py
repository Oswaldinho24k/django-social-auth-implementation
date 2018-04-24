from django.contrib import admin
from .models import Profile, Logro

# Register your models here.
class LogroAdmin(admin.ModelAdmin):
	list_display = ['name', 'user']
	list_filter = ['user']
	search_fields = ['name']


admin.site.register(Profile)
admin.site.register(Logro, LogroAdmin)