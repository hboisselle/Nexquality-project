from django.contrib import admin
from Nexquality.models import Project, ProjectUser, ProjectUserRole


class ProjectUserInline(admin.TabularInline):
    model = ProjectUser
    extra = 0


class ProjectModelAdmin(admin.ModelAdmin):
    inlines = [ProjectUserInline]
    list_filter = ['start_date']
    search_fields = ['name']

admin.site.register(Project, ProjectModelAdmin)
admin.site.register(ProjectUserRole, admin.ModelAdmin)
