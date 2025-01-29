from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # login api or token accessing api
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # api to refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # api to create user
    path('api/create-user', CreateUser.as_view(), name='create_user'),
    # api to create short note
    path('api/create-short-note', ShortNoteCreateView.as_view(), name='create_short_note'),
    # api to show the detail of short note created by logges user
    path('api/list-short-note', ListShortNotes.as_view(), name='list_short_note'),
    path('api/patch-short-note/<int:pk>', UpdateShortNote.as_view(), name='patch_short_note'),


]