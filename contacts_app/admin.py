from django.contrib import admin
from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'is_report', 'bug_type', 'date')

admin.site.register(Report, ReportAdmin)