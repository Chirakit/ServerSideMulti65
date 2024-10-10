from rest_framework import permissions

class SnippetPermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit and delete it.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS = GET, HEAD or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm("snippets.view_snippet")
        elif request.method == "POST":
            return request.user.has_perm("snippets.add_snippet")
        elif request.method == "PUT":
            return request.user.has_perm("snippets.change_snippet")
        elif request.method == "DELETE":
            return request.user.has_perm("snippets.delete_snippet")
        return False

    def has_object_permission(self, request, view, obj):
        if request.method == "PUT":
            return request.user.has_perm("snippets.change_snippet") and obj.created_by == request.user
        elif request.method == "DELETE":
            return request.user.has_perm("snippets.delete_snippet") and obj.created_by == request.user
        return False
