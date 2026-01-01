from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Profile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pic')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class LoginAttempt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='login_attempt')
    failed_attempts = models.IntegerField(default=0)
    last_failed = models.DateTimeField(null=True, blank=True)
    locked_until = models.DateTimeField(null=True, blank=True)

    def increment(self):
        now = timezone.now()
        self.failed_attempts = (self.failed_attempts or 0) + 1
        self.last_failed = now
        self.save()

    def reset(self):
        self.failed_attempts = 0
        self.last_failed = None
        self.locked_until = None
        self.save()

    def lock_for(self, hours=1):
        self.locked_until = timezone.now() + timedelta(hours=hours)
        self.save()

    def is_locked(self):
        return self.locked_until and self.locked_until > timezone.now()
