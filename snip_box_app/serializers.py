
from rest_framework import exceptions, serializers
from .models import *
from rest_framework.response import Response

class ShortNoteSerializer(serializers.ModelSerializer):
    tag_title = serializers.CharField(write_only=True)
    class Meta:
        model = ShortNote
        fields = ['tag_title', 'title', 'note']


    def create(self, validated_data):
        tag_title = validated_data.pop('tag_title')

        # Check if the tag already exists or create a new one
        tag, created = Tag.objects.get_or_create(title=tag_title)
        short_note = ShortNote.objects.create(tag_relation=tag, **validated_data)
        return short_note



class ShortNoteListSerializer(serializers.ModelSerializer):
    tag_title = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = ShortNote
        exclude = ['tag_relation','user']

    def get_user_name(self, obj):
        return obj.user.username if obj.user else None
    def get_tag_title(self, obj):
        return obj.tag_relation.title if obj.tag_relation else None


class ShortNoteOverviewByUserSerializer(serializers.ModelSerializer):
    tag_title = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    show_details = serializers.SerializerMethodField()
    
    class Meta:
        model = ShortNote
        exclude = ['tag_relation','user']

    def get_user_name(self, obj):
        return obj.user.username if obj.user else None
    def get_tag_title(self, obj):
        return obj.tag_relation.title if obj.tag_relation else None
    
    def get_show_details(self, obj):
        if self.context['filter_type'] == "user":
            return f"http://127.0.0.1:8000/api/read-short-note/{obj.id}"
        else:
            return f"http://127.0.0.1:8000/api/read-short-note/{obj.id}"


class ShortNoteUpdateSerializer(serializers.ModelSerializer):
    tag_title = serializers.CharField(write_only=True)
    show_tag_title = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = ShortNote
        fields = ['id','tag_title', 'title', 'note','show_tag_title','created_at','updated_at','user_name']

    def get_user_name(self, obj):
        return obj.user.username if obj.user else None
    def get_show_tag_title(self, obj):
        return obj.tag_relation.title if obj.tag_relation else None

    def update(self, instance, validated_data):
        tag_title = validated_data.pop('tag_title')
        tag, created = Tag.objects.get_or_create(title=tag_title)
        instance.tag_relation = tag
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
