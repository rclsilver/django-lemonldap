from django.core.exceptions import ImproperlyConfigured
from django.contrib import auth

class LemonldapAuthenticationMiddleware(object):
    """
    HTTP headers used :
      - user_infos key name
      - header key name
      - is required
      - default value if not provided
    """
    headers = [
        ('username', 'HTTP_AUTH_USER', True),
        ('firstname', 'HTTP_AUTH_FIRSTNAME', False, None),
        ('lastname', 'HTTP_AUTH_LASTNAME', False, None),
        ('mail', 'HTTP_AUTH_MAIL', False, None),
        ('is_superuser', 'HTTP_AUTH_SUPERUSER', False, 'false'),
        ('is_staff', 'HTTP_AUTH_STAFF', False, 'false'),
    ]
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.process_request(request)
        return response
    
    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The Django LemonLDAP auth middleware requires the"
                " authentication middleware to be installed. Edit your"
                " MIDDLEWARE_CLASSES setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the LemonLDAPMiddleware class.")
        
        user_infos = {}
        
        for header in self.headers:
            if header[2]:
                try:
                    user_infos[header[0]] = request.META[header[1]]
                except KeyError:
                    # If a required header doesn't exist then return (leaving
                    # request.user set to AnonymousUser by the AuthenticationMiddleware)
                    return
            else:
                user_infos[header[0]] = request.META.get(header[1], header[3] if 4 == len(header) else None)
        
        # If the user is already autheniticated and that user is the user we are
        # getting passed in the headers, then the correct user is already persisted
        # in the session and we don't need to continue.
        if request.user.is_authenticated():
            if request.user.username == self.clean_username(user_infos['username'], request):
                return
        
        user = auth.authenticate(lemonldap_user=user_infos)
        
        if user:
            # User is valid. Set request.user and persist user in the session
            # by logging the user in
            request.user = user
            auth.login(request, user)

    def clean_username(self, username, request):
        """
        Allows the backend to clean the username, if the backend defines a
        clean_username method.
        """
        
        backend_str = request.session[auth.BACKEND_SESSION_KEY]
        backend = auth.load_backend(backend_str)
        
        try:
            username = backend.clean_username(username)
        except AttributeError: # backend has no clean_username method
            pass
        
        return username

