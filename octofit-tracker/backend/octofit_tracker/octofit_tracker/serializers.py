from bson import ObjectId
from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class ObjectIdStringModelSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(getattr(obj, "_id", ""))

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
        return data


class UserProfileSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "name", "email", "level"]
        read_only_fields = ["id"]


class TeamSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "city"]
        read_only_fields = ["id"]


class ActivitySerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "user_email", "team_name", "activity_type", "duration_minutes"]
        read_only_fields = ["id"]


class LeaderboardEntrySerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = ["id", "user_email", "points", "rank"]
        read_only_fields = ["id"]


class WorkoutSuggestionSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = ["id", "user_email", "workout_name", "difficulty", "target"]
        read_only_fields = ["id"]
