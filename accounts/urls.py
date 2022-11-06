from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI, ChangePasswordView, LeadViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
img = DefaultRouter()
img.register(r'imageupload', views.ImageUploadViewSet)
from rest_framework import routers

from .views import LeadViewset

router = routers.DefaultRouter()
router.register('profile', LeadViewset, 'profile')


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/', include(router.urls)),
    path('api/', include(img.urls)),

    
]