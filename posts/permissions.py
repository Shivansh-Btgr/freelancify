from rest_framework.permissions import BasePermission

class CanViewDetailedPost(BasePermission):
    """
    Custom permission to only allow users with sufficient education level
    to view detailed post information.
    """
    
    def has_object_permission(self, request, view, obj):
        EDUCATION_HIERARCHY = {
            'highschool': 1,
            'associate': 2,
            'bachelor': 3,
            'master': 4,
            'phd': 5,
        }
        
        user_education_level = EDUCATION_HIERARCHY.get(request.user.max_education, 0)
        required_education_level = EDUCATION_HIERARCHY.get(obj.ed_req, 0)
        
        return user_education_level >= required_education_level