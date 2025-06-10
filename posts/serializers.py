from rest_framework import serializers
from .models import Post, Application
from accounts.models import CustomUser

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['role', 'description', 'salary', 'ed_req', 'job_type', 'experience_required', 'remote_allowed']
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class PostListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['role', 'description']

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['is_active']
        
    def validate(self, attrs):
        if 'is_active' not in attrs:
            raise serializers.ValidationError("Only 'is_active' field can be updated.")
        return attrs

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['post', 'resume', 'additional_info']
    
    def validate(self, attrs):
        user = self.context['request'].user
        post = attrs['post']
        
        if not post.is_active:
            raise serializers.ValidationError("Cannot apply to inactive posts.")
        
        if user.max_education < post.ed_req:
            education_levels = dict(user.EDUCATION_CHOICES)
            post_education_levels = dict(post.EDUCATION_CHOICES)
            raise serializers.ValidationError(
                f"Your education level ({education_levels.get(user.max_education, 'Unknown')}) "
                f"does not meet the minimum requirement ({post_education_levels.get(post.ed_req, 'Unknown')})."
            )
        
        if post.author == user:
            raise serializers.ValidationError("You cannot apply to your own post.")
        
        if Application.objects.filter(applicant=user, post=post).exists():
            raise serializers.ValidationError("You have already applied to this post.")
        
        return attrs
    
    def create(self, validated_data):
        validated_data['applicant'] = self.context['request'].user
        return super().create(validated_data)

class ApplicationListSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(source='post.role', read_only=True)
    company = serializers.CharField(source='post.company', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Application
        fields = ['id', 'post_title', 'company', 'status', 'status_display', 'applied_at']

class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']
    
    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in Application.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status. Choose from: {valid_statuses}")
        return value