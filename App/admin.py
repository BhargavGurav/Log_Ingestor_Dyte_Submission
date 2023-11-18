from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Log Ingestor'

class LogAdmin(admin.ModelAdmin):
    # search_fields = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit']
    list_display = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit']
    list_filter = ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit', 'metadata']


admin.site.register(Log, LogAdmin)

    

