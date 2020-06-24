from django.contrib import admin
from .models import User,ActivityPeriod


class UserAdmin(admin.ModelAdmin):
	list_display = ['id','email','real_name','tz']

class ActivityPeriodAdmin(admin.ModelAdmin):
	list_display = ['user','start_time','end_time']

admin.site.register(User,UserAdmin)
admin.site.register(ActivityPeriod,ActivityPeriodAdmin)