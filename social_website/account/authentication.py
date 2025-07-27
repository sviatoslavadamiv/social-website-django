from urllib.parse import urlparse

import requests
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

from account.models import Profile


class EmailAUthBackend:
    """
    Authentication using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, response, *args, **kwargs):
    """
    Create user profile for social authentication.
    """
    profile, created = Profile.objects.get_or_create(user=user)

    if backend.name == "google-oauth2":
        photo_url = response.get("picture")

        if photo_url and not profile.photo:
            try:
                response = requests.get(photo_url)
                response.raise_for_status()

                filename = urlparse(photo_url).path.split("/")[-1]
                ext = filename.split(".")[-1] if "." in filename else "jpg"
                final_name = f"{user.username}_google_photo.{ext}"

                profile.photo.save(
                    final_name, ContentFile(response.content), save=False
                )
            except Exception as e:
                raise e

        profile.save()
