from rest_framework import generics, permissions
from .models import Organization, Team, UserProfile, UserTeam
from .serializers import (
    OrganizationSerializer,
    TeamSerializer,
    UserProfileSerializer,
    UserTeamSerializer,
    RegisterSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserTeamListCreateView(generics.ListCreateAPIView):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserTeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer
    permission_classes = [permissions.IsAuthenticated]
