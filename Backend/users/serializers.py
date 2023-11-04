from rest_framework import serializers

from .models import User, Profile
from webcomic_app.models import Series
from webcomic_app.serializers import SeriesSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    series_created = serializers.SerializerMethodField()
    series_followed = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "username",
            "image",
            "series_created",
            "series_followed",
        )

    def get_series_created(self, obj):
        # Retrieve and serialize the series created by the user
        series_created = Series.objects.filter(creator=obj.user)
        return SeriesSerializer(series_created, many=True).data

    def get_series_followed(self, obj):
        # Retrieve and serialize the series followed by the user
        series_followed = Series.objects.filter(followers=obj.user)
        return SeriesSerializer(series_followed, many=True).data
