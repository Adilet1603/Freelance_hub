from modeltranslation.translator import TranslationOptions,register
from .models import Category, Project


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')