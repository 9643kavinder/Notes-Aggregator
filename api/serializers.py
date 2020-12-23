from rest_framework import serializers
from .models import NotePost


class NotePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotePost
        fields = ['title', 'content',]

    def create(self, validated_data):
        """
        Create and return a new `note` instance, given the validated data.
        """
        return NotePost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `note` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance