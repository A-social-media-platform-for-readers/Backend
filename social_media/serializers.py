from rest_framework import serializers
from .models import Post, Comment, InnerComment, Message
from users.serializers import UserSerializer


class PostSerializerCreate(serializers.ModelSerializer):
    """
    Post Serializer.
    """

    class Meta:
        model = Post
        fields = [
            "id",
            "content",
            "image",
            "video",
            "creat_time",
            "like_count",
            "you_liked",
            "comment_count",
            "user",
        ]
        extra_kwargs = {
            "like_count": {"read_only": True},
            "comment_count": {"read_only": True},
            "you_liked": {"read_only": True},
        }


class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "content",
            "image",
            "video",
            "creat_time",
            "like_count",
            "you_liked",
            "comment_count",
            "user",
        ]
        extra_kwargs = {
            "like_count": {"read_only": True},
            "you_liked": {"read_only": True},
            "comment_count": {"read_only": True},
        }


class CommentSerializerCreate(serializers.ModelSerializer):
    """
    Post Serializer.
    """

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "creat_time",
            "like_count",
            "you_liked",
            "inner_comment_count",
            "user",
            "post",
        ]
        extra_kwargs = {
            "like_count": {"read_only": True},
            "you_liked": {"read_only": True},
            "inner_comment_count": {"read_only": True},
        }


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "creat_time",
            "like_count",
            "you_liked",
            "inner_comment_count",
            "user",
            "post",
        ]
        extra_kwargs = {
            "like_count": {"read_only": True},
            "you_liked": {"read_only": True},
            "inner_comment_count": {"read_only": True},
        }


class InnerCommentSerializerCreate(serializers.ModelSerializer):
    """
    Post Serializer.
    """

    class Meta:
        model = InnerComment
        fields = [
            "id",
            "content",
            "creat_time",
            "like_count",
            "you_liked",
            "user",
            "comment",
        ]
        extra_kwargs = {
            "like_count": {"read_only": True},
            "you_liked": {"read_only": True},
        }


class InnerCommentSerializer(serializers.ModelSerializer):
    """
    InnerComment Serializer.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = InnerComment
        fields = [
            "id",
            "content",
            "creat_time",
            "like_count",
            "you_liked",
            "user",
            "comment",
        ]
        extra_kwargs = {
            "like_count": {"read_only": True},
            "you_liked": {"read_only": True},
        }


class MessageSerializerCreate(serializers.ModelSerializer):
    """
    Message Serializer.
    """

    class Meta:
        model = Message
        fields = ["id", "sender", "receiver", "content"]


class MessageSerializer(serializers.ModelSerializer):
    """
    Message Serializer.
    """

    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ["id", "sender", "receiver", "content", "creat_time"]
