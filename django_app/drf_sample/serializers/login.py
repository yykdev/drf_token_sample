from rest_framework import serializers

from drf_sample.models import Member


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=36, write_only=True)
    password = serializers.CharField(max_length=64, write_only=True)

    def validate(self, data):
        username = data['username']
        user = Member.objects.get(username=username)

        token, created = user.get_user_token(user.pk)

        ret = {
            'token': token.key,
            'user': {
                'user_pk': user.pk,
                'username': username,
            }
        }
        return ret