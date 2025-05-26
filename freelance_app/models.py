from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


class Skill(models.Model):
    skill_name = models.CharField(max_length=32)

    def __str__(self):
        return self.skill_name


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField()
    age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(17), MaxValueValidator(70)
    ], null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    ROLE_CHOICES = (
        ('client', 'client'),
        ('freelancer', 'freelancer'),
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='client')
    skills = models.ManyToManyField(Skill, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Network(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=32)
    network_link = models.URLField()

    def __str__(self):
        return f'{self.user.username} - {self.network_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Project(models.Model):
    title = models.CharField(max_length=72)
    description = models.TextField()
    budget = models.PositiveSmallIntegerField()
    deadline = models.DateTimeField()
    PROJECT_STATUS = (
        ('open', 'open'),
        ('in_progress', 'in_progress'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    )
    status = models.CharField(max_length=32, choices=PROJECT_STATUS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField(Skill, blank=True)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    proposed_budget = models.PositiveSmallIntegerField()
    proposed_deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.freelancer.username} - {self.project.title}'



class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_given')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_received')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.reviewer.role != 'client':
            raise ValidationError('Reviewer must be a client.')
        if self.target.role != 'freelancer':
            raise ValidationError('Target must be a freelancer.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)