from django.db import models
from django.contrib.auth.hashers import make_password


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    salt = 'shPaCQEEVd'

    def __str__(self):
        return self.first_name

    def save(self, **kwargs):
        self.password = make_password(self.password, self.salt)
        super(Member, self).save(**kwargs)
