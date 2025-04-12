from rest_framework.throttling import ScopedRateThrottle, UserRateThrottle

class OrderCreateThrottle(ScopedRateThrottle):
    scope = 'create_order'
    rate = '5/min'

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return None
        return self.cache_format % {
            'scope': self.scope,
            'ident': request.user.pk
        }

class PremiumUserThrottle(UserRateThrottle):
    scope = 'premium'

    def allow_request(self, request, view):
        if request.user.is_authenticated and request.user.is_premium:
            return True
        return super().allow_request(request, view)
