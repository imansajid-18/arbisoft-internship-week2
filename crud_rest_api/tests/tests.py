import pytest
from django.contrib.auth import get_user_model

from crud_rest_api.models import Note
from crud_rest_api.serializers import NoteSerializer

User = get_user_model()


@pytest.fixture
def test_user():
    User = get_user_model()
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="testpassword",
    )


# Unit Testing


@pytest.mark.django_db
def test_title_sanitization(test_user):
    data = {"title": "   My Clean Title   ", "description": "Valid description"}
    serializer = NoteSerializer(data=data)
    assert serializer.is_valid()
    serializer.save(user=test_user)
    note = Note.objects.first()
    assert note.title == "My Clean Title"


@pytest.mark.django_db
def test_reject_short_titles(test_user):
    data = {"title": "  Hi  ", "description": "Valid description"}
    serializer = NoteSerializer(data=data)
    assert not serializer.is_valid()
    assert "title" in serializer.errors


@pytest.mark.django_db
def test_reject_entirely_numeric_titles(test_user):
    data = {"title": "12345.67", "description": "Valid description"}
    serializer = NoteSerializer(data=data)
    assert not serializer.is_valid()
    assert "title" in serializer.errors


@pytest.mark.django_db
def test_valid_note_creation(test_user):
    data = {"title": "Perfect Title", "description": "Valid description"}
    serializer = NoteSerializer(data=data)
    assert serializer.is_valid()
    serializer.save(user=test_user)
    assert Note.objects.count() == 1
