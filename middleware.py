from django.conf import settings
from django.http import HttpResponsePermanentRedirect, get_host


class SSLMiddleware(object):

    def is_secure(self, request):
        if request.is_secure():
            return True

        if 'HTTP_X_FORWARDED_PROTO' in request.META:
            return request.META['HTTP_X_FORWARDED_PROTO'] == 'https'

        return False

    def redirect(self, request):
        url = 'https://%s%s' % (
            get_host(request),
            request.get_full_path()
        )
        secure_url = url.replace("http://", "https://")
        return HttpResponsePermanentRedirect(secure_url)

    def process_request(self, request):
        require_https = getattr(settings, 'HTTPS_REQUIRED', False)
        if require_https and not self.is_secure(request):
            return self.redirect(request)
