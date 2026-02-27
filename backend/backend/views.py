from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterJob, RegisterSerializer
from django.contrib.auth.models import User
@api_view(['GET'])
def hello_api(request):
    return Response({'messages':"Hello good morning!","IDEA":'Ignite','call':'attend'})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Registered Successfully"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_job(request):
    serializer = RegisterJob(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Registered Successfully"},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])

def basic_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)
        pas = User.objects.get(password=password)
        return Response({"message":"Login Success"},status=status.HTTP_200_OK)
    except Exception:
        return Response({"message":"invalid cred"},status=status.HTTP_400_BAD_REQUEST)