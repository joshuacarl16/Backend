# urls.py
from django.contrib import admin
from api import views
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register_user, name='register_user'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('topics/', views.view_topics, name='view_topics'),
    path('topics/<int:topic_id>/add_comment', views.add_comment, name='add_comment'),
    path('admin/add_category', views.admin_add_category, name='admin_add_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('categories/', views.view_category, name='view_category'),
    path('admin/topics/<int:topic_id>', views.admin_view_topic, name='admin_view_topic'),
    path('admin/users/<int:user_id>/topics', views.admin_view_user_topics, name='admin_view_user_topics'),
]

urlpatterns += router.urls