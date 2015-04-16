from django.contrib import admin
from Nexquality import models


class ProjectUserInline(admin.TabularInline):
    model = models.ProjectUser
    extra = 0


class ProjectModelAdmin(admin.ModelAdmin):
    inlines = [ProjectUserInline]
    list_filter = ['start_date']
    search_fields = ['name']


class MetricFieldAdmin(admin.ModelAdmin):
    exclude = ('category', 'name')


admin.site.register(models.Project, ProjectModelAdmin)
admin.site.register(models.ProjectUserRole, admin.ModelAdmin)
admin.site.register(models.MetricField, MetricFieldAdmin)
admin.site.register(models.Badge, admin.ModelAdmin)
admin.site.register(models.BadgeUser, admin.ModelAdmin)
