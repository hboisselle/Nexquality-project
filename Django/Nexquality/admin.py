from django.contrib import admin
from Nexquality.models import Project, ProjectUser, ProjectUserRole

admin.site.register(Project, admin.ModelAdmin)
admin.site.register(ProjectUserRole, admin.ModelAdmin)
