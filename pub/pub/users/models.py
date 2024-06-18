from django.contrib.auth.models import AbstractUser
from pub.models import CreateUpdateModel


class UserProfile(AbstractUser, CreateUpdateModel):
    pass
