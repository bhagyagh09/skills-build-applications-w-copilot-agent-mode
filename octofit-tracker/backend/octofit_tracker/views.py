from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'https://improved-space-waddle-6v9g76jg5g62x6rr-8000.app.github.dev/users/',
        'teams': 'https://improved-space-waddle-6v9g76jg5g62x6rr-8000.app.github.dev/teams/',
        'activity': 'https://improved-space-waddle-6v9g76jg5g62x6rr-8000.app.github.dev/activity/',
        'leaderboard': 'https://improved-space-waddle-6v9g76jg5g62x6rr-8000.app.github.dev/leaderboard/',
        'workouts': 'https://improved-space-waddle-6v9g76jg5g62x6rr-8000.app.github.dev/workouts/',
    })