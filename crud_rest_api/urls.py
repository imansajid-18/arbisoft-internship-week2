from django.urls import include, path
from rest_framework import routers

import crud_rest_api.views as views

router = routers.DefaultRouter()
router.register(r"notes", views.NotesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
