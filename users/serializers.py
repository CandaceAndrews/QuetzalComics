from rest_framework import serializers
from .models import User, Profile
from webcomic_app.models import Series


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class ProfileSerializer(serializers.ModelSerializer):
    series_created = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "user",
            "image",
            "series_created",
        )

    def get_series_created(self, obj):
        created_series = Series.objects.filter(creator=obj.user)
        series_serializer = SeriesSerializer(created_series, many=True)
        return series_serializer.data
