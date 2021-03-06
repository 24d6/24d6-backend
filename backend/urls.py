"""
  backend URL Configuration
"""
from django.conf.urls import url, include
from rest_framework import routers
from backend.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, 'user')
router.register(r'characters', views.CharacterViewSet, 'character')
router.register(r'groups', views.GroupViewSet, 'group')
router.register(r'runs', views.RunViewSet, 'run')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
