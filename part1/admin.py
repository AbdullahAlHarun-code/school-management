from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'School Management Administration'

from django.contrib import admin


admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"
