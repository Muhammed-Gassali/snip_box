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

   

class ListShortNotes(generics.ListAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteListSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request,**kwargs):
        try:
            user=self.request.user
            self.queryset = self.queryset.filter(user=user)
            response = super().get(request, **kwargs)
            return Response({'status':'success','response_code': status.HTTP_200_OK,'data':response.data})
        except Exception as e:
            message = str(e)
            return Response({'status': "failed",'response_code':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':message})


class UpdateShortNote(generics.UpdateAPIView):
    queryset = ShortNote.objects.all()
    serializer_class = ShortNoteUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ShortNote.objects.filter(user=self.request.user)
