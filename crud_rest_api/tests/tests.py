# Create your tests here.
import pytest
from crud_rest_api.models import Notes
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_note():
    dummy_user=User.objects.create_user(username="testuser", password="testpassword")
    note = Notes.objects.create(
        title="Test Note",
        description="This is a test note.",
        user=dummy_user
    )
    assert note.title == "Test Note"
    assert note.description == "This is a test note."
    assert note.user == dummy_user


@pytest.mark.django_db
def test_note_str_returns_title():
    dummy_user = User.objects.create_user(username="testuser1", password="testpassword")
    note = Notes.objects.create(
        title="Sample Note",
        description="Some description.",
        user=dummy_user
    )
    assert str(note) == "Sample Note"


@pytest.mark.django_db
def test_user_notes_related_name():
    dummy_user = User.objects.create_user(username="testuser2", password="testpassword")
    note = dummy_user.notes.create(
        title="Related Note",
        description="Related note description."
    )
    assert note.user == dummy_user
    assert dummy_user.notes.count() == 1
    assert dummy_user.notes.first() == note

