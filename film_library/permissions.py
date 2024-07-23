from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedForWrite(BasePermission):
    """
    Custom permission to only allow authenticated users to update or delete.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    