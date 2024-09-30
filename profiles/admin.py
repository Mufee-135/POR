from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Portfolio, Project

# Register the UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'skills']
    search_fields = ['user__username', 'bio', 'skills']
    list_filter = ['user__is_active']

# Register the Portfolio model
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['profile', 'title', 'description', 'link', 'created_at']
    search_fields = ['profile__user__username', 'title', 'description']
    list_filter = ['created_at']

# Register the Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['profile', 'title', 'description', 'link', 'created_at']
    search_fields = ['profile__user__username', 'title', 'description']
    list_filter = ['created_at']
