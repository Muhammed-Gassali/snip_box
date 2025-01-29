from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import  status,generics
from .models import *
from .serializers import *

"""
class to create new users, not added authentication here, because need to create new users
"""
class CreateUser(APIView):
    def post(self, request):
        User.objects.create_user(username=request.data['username'], password=request.data['password'])
        return Response({'status':"success",'response_code': status.HTTP_200_OK,'message':'user created successfully'})


# class CreateShortNote(generics.CreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = ShortNote.objects.all()
#     serializer_class = CreateShortNoteSerializer

#     def create(self, request, args, **kwargs):
#         tag, created = Tag.objects.get_or_create(title=request.data['tag_title'])
#         print(tag)
#         response = super().create(request, **kwargs)
#         return Response("hai")


class ShortNoteCreateView(generics.CreateAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def perform_create(self, serializer):
        # Assign the currently authenticated user to the short note
        serializer.save(user=self.request.user)

   
# class to list short note created by logged user
class ListShortNotes(generics.ListAPIView):
    queryset = ShortNote.objects.all()
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


class ListShortNoteByTagAndUser(generics.ListAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        self.queryset = self.queryset.filter(user=self.request.user,tag_relation=kwargs['tag_id'])
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})

class ListShortNoteByTag(generics.ListAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        self.queryset = self.queryset.filter(tag_relation=kwargs['tag_id'])
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


class OverviewShortNoteByUser(generics.ListAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteOverviewByUserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['filter_type'] = 'user'
        return context

    def get(self, request, **kwargs):
        self.queryset = self.queryset.filter(user=self.request.user)
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


class OverviewAllShortNote(generics.ListAPIView):
    queryset = ShortNote.objects.all().select_related('user','tag_relation')
    serializer_class = ShortNoteOverviewByUserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['filter_type'] = 'non_user'  # Example of custom context
        return context

    def get(self, request, **kwargs):
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


class ListTag(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        response = super().get(request, **kwargs)
        return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})


class ListShortAllNotes(generics.ListAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]


class ReadUpdateShortNote(generics.RetrieveUpdateAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)




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
        return Response(serializer.data, status=status.HTTP_200_OK)
