from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "user", "title", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    def validate_title(self, value):
        value = value.strip()
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError(
                "Title must contain actual words or letters, not just numbers."
            )
        return value

    def validate_description(self, value):
        value = value.strip()
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        if value.strip().isnumeric():
            raise serializers.ValidationError("Description cannot be entirely numeric.")
        return value
