from bson import ObjectId
from djongo import models


class UserProfile(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    level = models.CharField(max_length=50, default="beginner")

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "teams"

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField()
    team_name = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()

    class Meta:
        db_table = "activities"

    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class LeaderboardEntry(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField()
    points = models.IntegerField(default=0)
    rank = models.PositiveIntegerField()

    class Meta:
        db_table = "leaderboard"

    def __str__(self):
        return f"{self.user_email} ({self.points} pts)"


class WorkoutSuggestion(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField()
    workout_name = models.CharField(max_length=120)
    difficulty = models.CharField(max_length=50)
    target = models.CharField(max_length=120)

    class Meta:
        db_table = "workouts"

    def __str__(self):
        return f"{self.user_email} - {self.workout_name}"
