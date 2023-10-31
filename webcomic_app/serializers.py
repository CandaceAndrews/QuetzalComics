from rest_framework import serializers

from .models import Series


class SeriesSerializer(serializers.ModelSerializer):
    creator_username = serializers.SerializerMethodField()
    follower_usernames = serializers.SerializerMethodField()

    class Meta:
        model = Series
        fields = (
            "title",
            "description",
            "cover_image",
            "creator_username",
            "follower_usernames",
        )

    def get_creator_username(self, obj):
        return obj.creator.username  # Extract the username from the related User object

    def get_follower_usernames(self, obj):
        follower_usernames = [
            follower.username for follower in obj.followers.all()]
        return follower_usernames
