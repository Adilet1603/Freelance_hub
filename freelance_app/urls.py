from rest_framework import routers


from .views import *
from django.urls import path, include


router = routers.SimpleRouter()


router.register(r'networks', NetworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name= 'users_list'),
    path('users/me/', UserProfileOwnerRetrieveUpdateAPIView.as_view(), name='users_profile_me'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name= 'users_detail'),
    path('projects/', ProjectAPIView.as_view(), name = 'project_list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
    path('projects/<int:pk>/edit/', ProjectUpdateDestroyAPIView.as_view(), name = 'project_create'),
    path('categories/', CategoryListAPIView.as_view(), name = 'category_list' ),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name = 'category_detail'),
    path('skills/', SkillAPIView.as_view(), name = 'skill_list'),
    path('reviews/', ReviewCreateAPIView.as_view(), name = 'review_create'),
    path('projects/my/', ProjectOwnerListAPIView.as_view(), name= 'projects_my'),
    path('auth/register/', RegisterAPIView.as_view(), name='auth_register'),
    path('offers/', OfferCreateAPIView.as_view(), name='offer_create'),
    path('offers/my/', MyOffersListAPIView.as_view(), name='my_offers'),
    path('offers/<int:pk>/edit/', OfferUpdateDestroyAPIView.as_view(), name = 'offers_edit'),
    ]