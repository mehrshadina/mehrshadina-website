from django.contrib import admin
from .models import Post, Category, Image, Comment

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','pub_date')
    list_filter = ("category",)
    search_fields = ['title', 'content']
    #prepopulated_fields = {'category': ('title',)}

admin.site.register(Image)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)