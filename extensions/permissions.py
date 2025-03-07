from rest_framework.permissions import BasePermission

from user.models import User


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs.get('user_id')
        # 如果没有在 URL 中传递 user_id，则认为请求的是当前用户的资料
        if not user_id:
            return True
        # 如果传入了 user_id，则确保它和当前登录用户匹配
        return str(request.user.id) == str(user_id)