from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Save users individually to ensure proper primary key assignment
        users = [
            User(email='thundergod@mhigh.edu', name='Thunder God'),
            User(email='metalgeek@mhigh.edu', name='Metal Geek'),
            User(email='zerocool@mhigh.edu', name='Zero Cool'),
            User(email='crashoverride@mhigh.edu', name='Crash Override'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token'),
        ]
        for user in users:
            user.save()

        # Create teams with unique _id values
        teams = [
            Team(_id=ObjectId(), name='Blue Team'),
            Team(_id=ObjectId(), name='Gold Team')
        ]
        for team in teams:
            team.save()

        # Ensure users are saved before creating activities
        for user in users:
            user.save()

        # Create activities without ObjectId
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60),
            Activity(user=users[1], activity_type='Crossfit', duration=120),
            Activity(user=users[2], activity_type='Running', duration=90),
            Activity(user=users[3], activity_type='Strength', duration=30),
            Activity(user=users[4], activity_type='Swimming', duration=75),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard entries with team field
        leaderboard_entries = [
            Leaderboard(team=teams[0], score=100),
            Leaderboard(team=teams[1], score=90),
        ]
        for entry in leaderboard_entries:
            entry.save()

        # Create workouts with unique _id values
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))