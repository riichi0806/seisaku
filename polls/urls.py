from django.urls import path
from .views import PostListView,PostDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
#画像のアプロード
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)