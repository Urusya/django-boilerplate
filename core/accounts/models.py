from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'organization')
    
    # In Team model (optional shortcut)
    def get_members(self):
        return [ut.user for ut in self.user_teams.select_related('user')]

    def __str__(self):
        return f"{self.name} ({self.organization.name})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    # Remove this, move to custom through model
    # teams = models.ManyToManyField(Team, blank=True, related_name='members')

    def __str__(self):
        return self.user.username

class UserTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_teams')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='user_teams')
    role = models.CharField(max_length=100, blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'team')

    def __str__(self):
        return f"{self.user.username} in {self.team.name} as {self.role or 'Member'}"
