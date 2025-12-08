from django.contrib import admin
from . models import UserRequirement
from . models import AttendanceSession, AttendanceRecord

# Register your models here.
@admin.register(UserRequirement)
class UserRequirementAdmin(admin.ModelAdmin):
    list_display = ('Reg_Number', 'phone_number', 'department', 'level', 'email', 'first_name', 'last_name')
    search_fields = ('Reg_Number', 'phone_number', 'department', 'level', 'email', 'first_name', 'last_name')
    list_filter = ('department', 'level')

@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_open', 'opened_at', 'closes_at', 'code')

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status', 'ip')