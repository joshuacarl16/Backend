import json
from django.http import JsonResponse
from rest_framework import viewsets, status
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from api.serializer import CategorySerializer, TopicSerializer, UserSerializer
from .models import Category, Topic, Comment
from django.views.decorators.csrf import csrf_exempt


class UserViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

# @api_view(['POST'])
# def add_topic(request):
#     topic_data = request.data
#     category_id = topic_data.get('categoryId')
#     user_id = topic_data.get('userId')

#     category = Category.objects.filter(pk=category_id).first()
#     if not category:
#         return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)
    
#     user = get_user_model.objects.filter(pk=user_id).first()
#     if not user:
#         return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

#     topic = Topic.objects.create(
#         categoryName=category,
#         userId=user,
#         topicName=topic_data.get('topicName'),
#         content=topic_data.get('content'),
#         dateCreated=topic_data.get('dateCreated'),
#     )
#     serializer = TopicSerializer(topic)
#     return Response(serializer.data)

@api_view(['POST'])
def add_topic(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def add_topic(request):
#     serializer = TopicSerializer(data=request.data)
#     if serializer.is_valid():
#         category_id = request.data.get('category').get('id')
#         category = get_object_or_404(Category, id=category_id)
#         topic = Topic(category=category, **serializer.validated_data)
#         topic.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
@api_view(['POST', 'GET'])
def create_topic(request):
    if request.method == 'POST':
        try:
            topicName = request.POST['topicName']
            content = request.POST['content']
        except MultiValueDictKeyError as e:
            return Response({"error": str(e)})
        category_id = request.POST['category']
        category = get_object_or_404(Category, id=category_id)
        Topic.objects.create(topicName=topicName, content=content, category=category, user=request.user)
        return Response({"message": "Topic created successfully!"})
    else:
        categories = Category.objects.all().values()
        return Response({'categories': list(categories)})

@csrf_exempt
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context={'request': request}).data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['POST'])
# def add_topic(request):
#     if request.method == 'POST':
#         category_name = request.data.get('categoryName')
#         category = get_object_or_404(Category, categoryName=category_name)

#         topic_data = request.data.copy()
#         topic_data['categoryName'] = category.id
#         serializer = TopicSerializer(data=topic_data)
        
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response({"message": "Topic created successfully!"}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
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

@api_view(['POST'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @login_required
@api_view(['GET'])
def view_category(request):
    categories = Category.objects.all().values()
    return Response({'categories': list(categories)})

@api_view(['GET'])
def admin_view_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    topic_info = {"topicName": topic.topicName, "content": topic.content, "category": topic.category.name, "user": topic.user.username}
    return Response({'topic': topic_info})

@api_view(['GET'])
def admin_view_user_topics(request, user_id):
    user = get_object_or_404(user, id=user_id)
    topics = Topic.objects.filter(user=user).values()
    return Response({'topics': list(topics)})
