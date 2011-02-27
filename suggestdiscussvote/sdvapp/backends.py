class AuthorizationBackend():
    supports_object_permissions = True

    def authenticate(self, username=None, password=None):
        return None

    def get_user(self, user_id):
        return None

    def has_perm(self, user_obj, perm, obj=None):
        if obj is not None and perm == 'sdvapp.change_suggestion':
            return obj.suggested_by == user_obj
        else:
            return False

