from django.core.exceptions import PermissionDenied


class UserIsOwnerOrManagerMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user.has_perm('mailing_service.can_deactivate_mailing') or self.request.user == obj.owner:
            return obj
        raise PermissionDenied
