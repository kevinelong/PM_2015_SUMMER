from django.contrib import admin
from commentbox.models import CommentBox, BlogPost

class CommentBoxAdmin(admin.ModelAdmin):
    pass
admin.site.register(CommentBox, CommentBoxAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogPost, BlogPostAdmin)
