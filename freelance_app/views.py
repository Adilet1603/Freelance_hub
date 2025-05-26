from django_filters.rest_framework import DjangoFilterBackend
from .serializer import *
from .models import *
from rest_framework import viewsets, generics, filters, permissions
from django.contrib.auth.models import User


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer


class UserProfileDetailAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer


class UserProfileOwnerRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileOwnerRetrieveUpdateSerializer

    def get_object(self):
        return self.request.user.userprofile


class SkillAPIView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class OfferCreateAPIView(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferCreateSerializer

    def offer_create(self, serializer):
        serializer.save(freelancer=self.request.user)

class MyOffersListAPIView(generics.ListAPIView):
    serializer_class = OfferSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Offer.objects.filter(freelancer=self.request.user)

class OfferUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferUpdateDestroySerializer


class ProjectAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'budget', 'skills_required', 'category']
    ordering_fields = ['budget', 'created_at', 'deadline']
    ordering = ['-created_at']
    # permission_classes = []






class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

class ProjectUpdateDestroyAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProjectOwnerListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectOwnerSerializer()
    permission_classes = [permissions.IsAuthenticated]


class RegisterAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer

