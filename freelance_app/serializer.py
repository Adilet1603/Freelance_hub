from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *




class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name']

class UserProfileListSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'role', 'skills']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'profile_image','first_name', 'last_name','age', 'role',
                  'skills', 'email', 'phone_number',  ]

class UserProfileOwnerRetrieveUpdateSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'profile_image','first_name', 'last_name','age', 'role',
                  'skills', 'email', 'phone_number',]




class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class ProjectSerializer(serializers.ModelSerializer):
    client = UserProfileListSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ['client','title', 'deadline', 'status', 'description', 'budget',
                  'category', 'skills_required', 'created_at', 'deadline']



class ProjectUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'freelancer', 'project', 'message', 'proposed_budget', 'created_at']
        read_only_fields = ['freelancer', 'created_at']


class OfferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'freelancer', 'project', 'message', 'proposed_budget', 'created_at']
        read_only_fields = ['freelancer', 'created_at']


class OfferUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['project', 'target', 'rating', 'comment', 'created_at']

class ProjectDetailSerializer(serializers.ModelSerializer):
    client = UserProfileListSerializer(read_only=True)
    category = CategoryListSerializer(read_only=True)
    skills_required = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['client','title', 'description', 'budget', 'deadline',
                  'status', 'category', 'skills_required']


class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


