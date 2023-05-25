from rest_framework import fields, serializers
from django.contrib.auth import get_user_model
from .models import Category, Topic, Comment


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={
            "min_length": f"Password must be longer than 8 characters."
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={
            "min_length": f"Password must be longer than 8 characters."
        }
    )
    class Meta:
        model = get_user_model()
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data
    
    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()
        
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['categoryName']

class TopicSerializer(serializers.ModelSerializer):
    categoryName = serializers.StringRelatedField()
    
    class Meta:
        model = Topic
        fields = ['id', 'categoryName', 'topicName', 'content', 'dateCreated']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    topic = TopicSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'topic', 'content', 'created_at']