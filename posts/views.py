from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework import generics, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .permissions import CanViewDetailedPost
from .models import Post, Application
from .serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer, PostUpdateSerializer, ApplicationCreateSerializer, ApplicationListSerializer, ApplicationStatusUpdateSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Create a new job post",
        description="Create a new job posting with role, requirements, and salary information",
        tags=["Job Posts"],
        responses={201: PostDetailSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_active = True)
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['role', 'salary']
    
    @extend_schema(
        summary="List all active job posts",
        description="Get a list of all active job postings. Can be searched by role or salary.",
        tags=["Job Posts"],
        responses={200: PostListSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_active = True)
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated, CanViewDetailedPost]
    lookup_field = 'pk'
    
    @extend_schema(
        summary="Get job post details",
        description="Get detailed information about a specific job post. Requires authentication and appropriate education level.",
        tags=["Job Posts"],
        responses={200: PostDetailSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MyPostsView(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Get my job posts",
        description="Get all job posts created by the authenticated user",
        tags=["My Posts"],
        responses={200: PostListSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)

class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']
    
    @extend_schema(
        summary="Update my job post",
        description="Update a job post created by the authenticated user",
        tags=["My Posts"],
        responses={200: PostUpdateSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)

class PostApplyView(generics.CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Apply to a job post",
        description="Submit an application for a specific job post with cover letter and resume",
        tags=["Applications"],
        responses={201: ApplicationCreateSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        post_id = self.kwargs.get('pk')
        post = Post.objects.get(pk=post_id)
        serializer.save(applicant=self.request.user, post=post)

class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Get my applications",
        description="Get all job applications submitted by the authenticated user",
        tags=["Applications"],
        responses={200: ApplicationListSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)

class PostApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Get applications for my job post",
        description="Get all applications for a job post created by the authenticated user",
        tags=["My Posts"],
        responses={200: ApplicationListSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        post = Post.objects.get(pk=post_id, created_by=self.request.user)
        return Application.objects.filter(post=post)

class ApplicationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ApplicationStatusUpdateSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']
    
    @extend_schema(
        summary="Update application status",
        description="Update the status of an application for your job post (accept/reject)",
        tags=["My Posts"],
        responses={200: ApplicationStatusUpdateSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    def get_queryset(self):
        return Application.objects.filter(post__created_by=self.request.user)