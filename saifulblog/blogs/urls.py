from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<slug:category_slug>/', views.blog, name='category_wise_post'),
    # path('add_post/', views.add_post, name="add_post"),
    path('add_post/', login_required(views.AddPost.as_view()), name="add_post"),
    # path('edit/<int:id>', views.edit_post, name="edit_post"),
    path('edit/<int:id>/', views.EditPost.as_view(), name="edit_post"),
    # path('delete/<int:id>', views.delete_post, name="delete_post"),
    path('delete/<int:id>/', views.DeletePost.as_view(), name="delete_post"),
    path('details/<int:id>/', views.PostDetails.as_view(), name="post_details"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)