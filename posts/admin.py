from django.contrib import admin
from .models import Post, Application

admin.site.register(Post)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'post', 'status', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['applicant__username', 'post__role']
    readonly_fields = ['applied_at']