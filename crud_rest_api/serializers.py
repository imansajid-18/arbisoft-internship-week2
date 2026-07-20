from rest_framework import serializers

from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        if value.isnumeric():
            raise serializers.ValidationError("Title cannot be entirely numeric.")
        return value
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        if value.isnumeric():
            raise serializers.ValidationError("Description cannot be entirely numeric.")
        return value
    def validate_user(self, value):
        if value is None:
            raise serializers.ValidationError("User field cannot be null.")
        return value
