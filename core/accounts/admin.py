from django.contrib import admin
from .models import Organization, Team, UserProfile, UserTeam

# Standard model registration
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(UserProfile)

# Custom admin for UserTeam
@admin.register(UserTeam)
class UserTeamAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'role', 'joined_at')
    list_filter = ('team', 'role')
