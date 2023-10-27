from rest_framework import serializers
from .models import Series


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = (
            "title",
            "description",
            "cover_image",
            "creator"
            "followers",
        )
