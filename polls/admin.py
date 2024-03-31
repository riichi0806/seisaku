
from django.contrib import admin
from .models import Post
 
#管理画面の記事一覧で表示する列を指定
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at','thumbnail')
 
#Postモデルに対応する管理機能を定義
admin.site.register(Post, PostAdmin)