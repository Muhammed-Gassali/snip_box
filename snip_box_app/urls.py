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
    # api to show the list of short note created by logges user
    path('api/list-short-note', ListShortNotes.as_view(), name='list_short_note'),
    # api to show the list all short note
    path('api/list-all-short-note', ListShortAllNotes.as_view(), name='list_all_short_note'),
    # use patch to update short note
    path('api/patch-short-note/<int:pk>', ReadUpdateShortNote.as_view(), name='patch_short_note'),
    # use get to read short note 
    path('api/read-short-note/<int:pk>', ReadUpdateShortNote.as_view(), name='patch_short_note'),
    path('api/delete-short-note/<int:pk>', ShortNoteDeleteView.as_view(), name='shortnote-delete'),
    path('api/list-short-note-by-tag-and-user/<int:tag_id>', ListShortNoteByTagAndUser.as_view(), name='list_short_note_by_tag_and_user'),
    path('api/list-short-note-by-tag/<int:tag_id>', ListShortNoteByTag.as_view(), name='list_short_note_by_tag'),
    path('api/list-tag', ListTag.as_view(), name='list_tag'),
    path('api/overview-short-note-by-user', OverviewShortNoteByUser.as_view(), name='overview_short_note_by_user'),
    path('api/overview-all-short-notes', OverviewAllShortNote.as_view(), name='overview_all_short_notes'),



]