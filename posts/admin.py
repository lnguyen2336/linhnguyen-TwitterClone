from django.contrib import admin

# Register your models here.

from .models import Post
class PostAdmin(admin.ModelAdmin):
   list_display = ['name' , 'body' ]
admin.site.register(Post , PostAdmin)
