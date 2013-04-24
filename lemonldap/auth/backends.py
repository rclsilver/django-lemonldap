from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import get_user_model

class LemonldapUserBackend(RemoteUserBackend):
    # Create a User object if not already in the database?
    create_unknown_user = True

    def authenticate(self, lemonldap_user):
        """
        The user informations passed as ``lemonldap_user`` dictionnary is considered
        as trusted. This method simply returns the ``User`` object with the given
        informations, creating a new ``User`` object if ``create_unknown_user`` is ``True``.

        Returns None if ``create_unknown_user`` is ``False`` and a ``User`` object with
        the given informations is not found in the database.
        """
        if not lemonldap_user:
            return
        user = None
        username = self.clean_username(lemonldap_user['username'])
        
        UserModel = get_user_model()
        
        if self.create_unknown_user:
            user, created = UserModel.objects.get_or_create(**{UserModel.USERNAME_FIELD: username})
            if created:
                user = self.configure_user(user, lemonldap_user)
        else:
            try:
                user = UserModel.objects.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                pass
        return user

    def clean_username(self, username):
        """
        Performs any cleaning on the "username" prior to using it to get or
        create the user object.  Returns the cleaned username.

        By default, returns the username unchanged.
        """
        return username

    def configure_user(self, user, user_infos):
        """
        Configures a user after creation and returns the updated user.
        """
        if user_infos['mail']: user.email = user_infos['mail']
        if user_infos['firstname']: user.first_name = user_infos['firstname']
        if user_infos['lastname']: user.last_name = user_infos['lastname']
        user.is_superuser = 'true' == user_infos['is_superuser'] or user_infos['is_superuser'] is True
        user.is_staff = 'true' == user_infos['is_staff'] or user_infos['is_staff'] is True
        user.save()
        return user

