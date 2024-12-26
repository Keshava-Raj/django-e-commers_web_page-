
from django.contrib.auth.backends import BaseBackend
from .models import Provider_register



class providerLogin(BaseBackend):
    def authentication(self, request, email=None, password=None):
        try:
            user = Provider_register.objects.get(email=email)
            if user.check_password(password):
                return user
        except Provider_register.DoesNotExist:
            return None