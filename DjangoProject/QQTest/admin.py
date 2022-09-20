from django.contrib import admin

# Register your models here.
from QQTest.models import Application,Interface



# class ProjectAdmin(admin.ModelAdmin):
#     list_display =("service_id","application_type","interface_name")
#
# admin.site.register(Interface,ProjectAdmin)

# Global
admin.site.site_header = "PEGA"
admin.site.site_title = "Daimer"