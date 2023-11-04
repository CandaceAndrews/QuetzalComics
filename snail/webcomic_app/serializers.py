from rest_framework import serializers
from taggit.models import Tag

from .models import Series


class SeriesSerializer(serializers.ModelSerializer):
    creator_username = serializers.SerializerMethodField()
    follower_usernames = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(
        many=True, slug_field='name', queryset=Tag.objects.all())

    class Meta:
        model = Series
        fields = (
            "title",
            "description",
            "cover_image",
            "creator_username",
            "follower_usernames",
            "tags",
        )

    def get_creator_username(self, obj):
        return obj.creator.username  # Extract the username from the related User object

    def get_follower_usernames(self, obj):
        follower_usernames = [
            follower.username for follower in obj.followers.all()]
        return follower_usernames
