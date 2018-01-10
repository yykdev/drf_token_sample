from rest_framework import serializers

from drf_sample.models import Member


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()

    class Meta:
        model = Member
        fields = (
            'username',
        )