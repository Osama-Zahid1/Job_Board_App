from django.contrib.auth.backends import ModelBackend
from .models import Seekermodel, Recruitermodel

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if '@' in username:
            # If username is an email, try to authenticate as a seeker
            try:
                user = Seekermodel.objects.get(email=username)
            except Seekermodel.DoesNotExist:
                # If user not found among seekers, try to authenticate as a recruiter
                try:
                    user = Recruitermodel.objects.get(email=username)
                except Recruitermodel.DoesNotExist:
                    return None
        else:
            # If username is not an email, try to authenticate as a seeker
            try:
                user = Seekermodel.objects.get(username=username)
            except Seekermodel.DoesNotExist:
                # If user not found among seekers, try to authenticate as a recruiter
                try:
                    user = Recruitermodel.objects.get(username=username)
                except Recruitermodel.DoesNotExist:
                    return None

        if user.check_password(password):
            return user
        return None
