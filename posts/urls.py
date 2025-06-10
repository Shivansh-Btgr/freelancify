from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('my-posts/', views.MyPostsView.as_view(), name='my_posts'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/apply/', views.PostApplyView.as_view(), name='post_apply'),
    path('<int:pk>/applications/', views.PostApplicationsView.as_view(), name='post_applications'),
    path('my-applications/', views.MyApplicationsView.as_view(), name='my_applications'),
    path('<int:post_pk>/applications/<int:pk>/status/', views.ApplicationStatusUpdateView.as_view(), name='application_status_update'),
]