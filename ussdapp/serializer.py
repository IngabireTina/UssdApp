from rest_framework import serializers
from .models import UssdApplication, Task


class UssdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
