from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "Adding customers not allowed."

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()



class IsOwner(BasePermission):
    def has_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
