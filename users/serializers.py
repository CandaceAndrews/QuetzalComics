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
    series_created = serializers.SerializerMetaclass("get_created_series")

    class Meta:
        model = Profile
        fields = (
            "user",
            "image",
            "series_created",
        )

    def get_created_series(self, obj):
        queryset = Series.objects.filter(creator=obj)
