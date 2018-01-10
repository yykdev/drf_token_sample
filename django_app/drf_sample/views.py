from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_sample.serializers.login import LoginSerializer
from drf_sample.serializers.user import UserSerializer

User = get_user_model()


class LoginView(APIView):

    def get(self, request, format=None):
        return render(request, 'login.html')

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            ret = serializer.validated_data
        return Response(ret)


class UserDetail(APIView):

    def post(self, request, format=None):
        user = User.objects.get(pk=request.user.id)
        print(user.username)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)