from django.db.models import fields
from rest_framework import serializers
from .models import Tree

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ('title', 'url', 'content', 'level', 'type', 'active', 
                'created_at', 'updated_at')