from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views','likes')
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'url')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website', 'picture',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)