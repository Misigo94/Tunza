from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'
