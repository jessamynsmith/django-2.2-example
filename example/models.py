from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthday = models.DateField()
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return '{} ({})'.format(self.user.username, self.nickname)
