from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list'),
    path('teams/', TeamListCreateView.as_view(), name='team-list'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('user-teams/', UserTeamListCreateView.as_view(), name='userteam-list'),
    path('user-teams/<int:pk>/', UserTeamDetailView.as_view(), name='userteam-detail'),
]
