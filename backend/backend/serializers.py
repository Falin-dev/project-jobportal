from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Job

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password','phone']

class RegisterJob(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id","title","description","salary","posted_on"]