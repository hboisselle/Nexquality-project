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


class ProfileModelAdmin(admin.ModelAdmin):
    exclude = ('user',)


class BadgeModelAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'category', 'score', 'image', 'conditions', 'given_once')


admin.site.register(models.Project, ProjectModelAdmin)
admin.site.register(models.ProjectUserRole, admin.ModelAdmin)
admin.site.register(models.MetricField, MetricFieldAdmin)
admin.site.register(models.Badge, BadgeModelAdmin)
admin.site.register(models.BadgeUser, admin.ModelAdmin)
admin.site.register(models.BadgeCategory, admin.ModelAdmin)
admin.site.register(models.Profile, ProfileModelAdmin)
admin.site.register(models.ProfileType, admin.ModelAdmin)
