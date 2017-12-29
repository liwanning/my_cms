from django.contrib import admin
from cms.models import Category,Story
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title','owner','status','created','modified')
    search_fields = ('title','markdown_content')
    list_filter = ('status','owner','created','modified')
    prepopulated_fields = {'slug':('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('label',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Story,StoryAdmin)
