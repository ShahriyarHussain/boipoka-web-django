from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
# from django.contrib.auth.models import User
# from .models import Profile
# Create your views here.


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.data.get('user')
        if not user:
            return Response({'response': 'error',
                            'message': 'No data found'})
        serializer = UserSerializerWithToken(data=user)

        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({'response': 'error', 'message': serializer.errors})

        return Response({'response': 'successs', 'message': 'user created successfully'})


# class ProfileView(viewsets.ModelViewSet):
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()
