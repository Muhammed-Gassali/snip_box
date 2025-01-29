from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # api to create user
    path('api/create-user', CreateUser.as_view(), name='create_user'),

    # Authentication APIs
    # login api or token accessing api - requirement 1
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # api to refresh token - requirement 2
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #CRUD APIs
    # requirement 1 - overview api - list snippets created by logged user
    path('api/overview-short-note-by-user', OverviewShortNoteByUser.as_view(), name='overview_short_note_by_user'),
    # requirement 1 - overview api - list all snippets
    path('api/overview-all-short-notes', OverviewAllShortNote.as_view(), name='overview_all_short_notes'),
    # requirement 2 -  api to create short note
    path('api/create-short-note', ShortNoteCreateView.as_view(), name='create_short_note'),
    # requirement 3 - use get to read short note 
    path('api/read-short-note/<int:pk>', ReadUpdateShortNote.as_view(), name='patch_short_note'),
    # api to show the list of short note created by logges user
    path('api/list-short-note-by-user', ListShortNotesByUser.as_view(), name='list_short_note_by_user'),
    # api to show the list all short note
    path('api/list-all-short-note', ListShortAllNotes.as_view(), name='list_all_short_note'),
    # requirement 4 -use patch to update short note
    path('api/patch-short-note/<int:pk>', ReadUpdateShortNote.as_view(), name='patch_short_note'),
    # requirement 5 - use delete method to delete short note
    path('api/delete-short-note/<int:pk>', ShortNoteDeleteView.as_view(), name='shortnote-delete'),
    # requirement 6 - list tags
    path('api/list-tag', ListTag.as_view(), name='list_tag'),
    # requirement 7 - list short notes by tags create by logged user
    path('api/list-short-note-by-tag-and-user/<int:tag_id>', ListShortNoteByTagAndUser.as_view(), name='list_short_note_by_tag_and_user'),
    # requirement 7 - list all short notes by tags
    path('api/list-short-note-by-tag/<int:tag_id>', ListShortNoteByTag.as_view(), name='list_short_note_by_tag'),

    # sub api for requirement 1 - to read short note 
    path('api/read-all-short-note/<int:pk>', ReadAllShortNote.as_view(), name='read_all_short_note'),



    
    
    
    
    
    



]