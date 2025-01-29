from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import  status,generics
from .models import *
from .serializers import *

"""
class to create new users, not added authentication here, because need to create new users to test apis
"""
class CreateUser(APIView):
    def post(self, request):
        User.objects.create_user(username=request.data['username'], password=request.data['password'])
        return Response({'status':"success",'response_code': status.HTTP_200_OK,'message':'user created successfully'})


"""
This class provides an API endpoint to retrieve a list of short notes created by the logged-in user. It includes the following features:

Total Count of Short Notes: The total number of short notes is provided through the count variable in the response data.
Hyperlink to User-Created short notes: Each response includes a hyperlink to view details of short note created by the logged-in user. This feature is included to enhance navigation, as the API only permits access to short notes created by the logged-in user
"""
class OverviewShortNoteByUser(generics.ListAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteOverviewByUserSerializer
    permission_classes = [IsAuthenticated]

    # sending content to serializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['filter_type'] = 'user'
        return context

    def get(self, request, **kwargs):
        self.queryset = self.queryset.filter(user=self.request.user)
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


"""
This class provides an API endpoint to retrieve a list of all short notes. It includes the following features:

Total Count of Short Notes: The total number of short notes is provided through the count variable in the response data.
Hyperlink to User-Created short notes: Each response includes a hyperlink to view details of short notes
"""
class OverviewAllShortNote(generics.ListAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteOverviewByUserSerializer
    permission_classes = [IsAuthenticated]

    # sending content to serializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['filter_type'] = 'non_user'
        return context

    def get(self, request, **kwargs):
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


"""
This class facilitates the creation of short notes with associated tags.
It checks if a tag already exists; if so, it maps the tag to the note. If the tag does not exist, 
the class creates the tag and maps it accordingly. The logic for tag creation and mapping is implemented in the serializer section
"""
class ShortNoteCreateView(generics.CreateAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the currently authenticated user to the short note
        serializer.save(user=self.request.user)


"""
class to read and patch short note details. in case of read, use get method and will get logged user created note and use patch method to patch data.
update logic are addedd in serializer section. like in creation, tags are fetching from database if it existed or create a new one if it is not get from database
"""
class ReadUpdateShortNote(generics.RetrieveUpdateAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

   
"""
class to list short note created by logged user
"""
class ListShortNotesByUser(generics.ListAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,**kwargs):
        try:
            self.queryset = self.queryset.filter(user=self.request.user)
            response = super().get(request, **kwargs)
            return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})
        except Exception as e:
            message = str(e)
            return Response({'status': "failed",'response_code':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':message})

"""
class to list all short notes
"""
class ListShortAllNotes(generics.ListAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]


"""
class to delete short notes created by logged user and will list rest of short notes created by logged user
"""
class ShortNoteDeleteView(generics.DestroyAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Ensure users can only delete their own notes"""
        return self.queryset.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        """Delete the instance and return the updated list of notes"""
        instance = self.get_object() 
        self.perform_destroy(instance)
        remaining_notes = self.get_queryset()
        serializer = self.get_serializer(remaining_notes, many=True)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':serializer.data})

"""
class to list tags
"""
class ListTag(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = [IsAuthenticated]

    # added get function to customize the response
    def get(self, request, **kwargs):
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


"""
class to list short notes under a tag created by logged user
"""
class ListShortNoteByTagAndUser(generics.ListAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        self.queryset = self.queryset.filter(user=self.request.user,tag_relation=kwargs['tag_id'])
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


"""
class to list all short notes under a tag
"""
class ListShortNoteByTag(generics.ListAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        self.queryset = self.queryset.filter(tag_relation=kwargs['tag_id'])
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


"""
class to read a short note. used to add hyperlink while listed all short notes in requirement 1
"""
class ReadAllShortNote(generics.RetrieveUpdateAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteUpdateSerializer
    permission_classes = [IsAuthenticated]







