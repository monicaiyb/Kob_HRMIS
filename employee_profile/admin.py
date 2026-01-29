from django.contrib import admin
from .models import Employee

# it will show on admin page "superuser"
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'department', 'date_of_birth')
    list_filter = ('designation', 'department', 'date_of_birth')
    search_fields = ('first_name','last_name', 'email', 'department', 'date_of_birth')
    date_hierarchy = 'date_of_birth'
    ordering = ('-date_of_birth',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name','last_name', 'email', 'phonenumber', 'address', 'department', 'role', 'date_of_birth')
        }),
        ('Joining Information', {
            'fields': ('date_of_birth',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['date_of_birth']
        return []

admin.site.register(Employee, EmployeeAdmin)
# Register your models here.
