from django.contrib import admin
from Nexquality.models import Project, ProjectUser


class ProjectTeamInline(admin.TabularInline):
    model = ProjectUser
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    """
    class for admin project management
    """

admin.site.register(Project, admin.ModelAdmin)
