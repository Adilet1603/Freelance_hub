from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

class NetworkInline(admin.TabularInline):
    model = Network
    extra = 1

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [NetworkInline]


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

@admin.register(Category,)
class CategoryAdmin(TranslationAdmin):
    inlines = [ProjectInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Skill)
admin.site.register(Offer)
admin.site.register(Review)
admin.site.register(Network)