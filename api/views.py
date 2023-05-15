from rest_framework import viewsets, status
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from api.serializer import UserSerializer
from .models import Category, Topic, Comment
from django.views.decorators.csrf import csrf_exempt


class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

@login_required
@csrf_exempt
@api_view(['POST', 'GET'])
def create_topic(request):
    if request.method == 'POST':
        try:
            title = request.POST['title']
            content = request.POST['content']
        except MultiValueDictKeyError as e:
            return Response({"error": str(e)})
        category_id = request.POST['category']
        category = get_object_or_404(Category, id=category_id)
        Topic.objects.create(title=title, content=content, category=category, user=request.user)
        return Response({"message": "Topic created successfully!"})
    else:
        categories = Category.objects.all().values()
        return Response({'categories': list(categories)})

@api_view(['GET'])
def view_topics(request):
    topics = Topic.objects.all().values()
    return Response({'topics': list(topics)})

@csrf_exempt
@api_view(['POST', 'GET'])
def add_comment(request, topic_id):
    if request.method == 'POST':
        content = request.POST['content']
        topic = get_object_or_404(Topic, id=topic_id)
        Comment.objects.create(content=content, topic=topic, user=request.user)
        return Response({"message": "Comment added successfully!"})
    else:
        return Response({"message": "Unable to post comment."})

@csrf_exempt
@api_view(['POST', 'GET'])
def admin_add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return Response({"message": "Category added successfully!"})
    else:
        return Response({"message": "Unable to add category."})

# @api_view(['GET'])
# def view_category(request):
#     category_id = request.POST['category']
#     Category = get_object_or_404(Category, id=category_id)
#     category_info = {"name"}
#     return Response({'category': category_info})
@login_required
@api_view(['GET'])
def view_category(request):
    categories = Category.objects.all().values()
    return Response({'categories': list(categories)})

@api_view(['GET'])
def admin_view_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    topic_info = {"title": topic.title, "content": topic.content, "category": topic.category.name, "user": topic.user.username}
    return Response({'topic': topic_info})

@api_view(['GET'])
def admin_view_user_topics(request, user_id):
    user = get_object_or_404(user, id=user_id)
    topics = Topic.objects.filter(user=user).values()
    return Response({'topics': list(topics)})
