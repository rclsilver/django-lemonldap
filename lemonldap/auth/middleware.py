class LemonldapAuthenticationMiddleware(object):
    headers = [
        ('username', 'HTTP_AUTH_USER'),
        ('firstname', 'HTTP_AUTH_FIRSTNAME'),
        ('lastname', 'HTTP_AUTH_LASTNAME'),
        ('mail', 'HTTP_AUTH_MAIL'),
        ('is_superuser', 'HTTP_AUTH_SUPERUSER'),
        ('is_staff', 'HTTP_AUTH_STAFF'),
    ]
    
    def process_request(self, request):
        pass
