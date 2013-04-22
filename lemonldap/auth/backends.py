from django.contrib.auth.backends import RemoteUserBackend

class LemonldapUserBackend(RemoteUserBackend):
    # Create a User object if not already in the database?
    create_unknown_user = False

    def authenticate(self, lemonldap_user):
        pass
