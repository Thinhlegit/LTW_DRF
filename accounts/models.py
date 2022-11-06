from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models.deletion import CASCADE
class ImageUpload(models.Model):
    title = models.CharField(max_length=50)
    # images = models.ImageField('images')
    images = ResizedImageField(scale=0.5, quality=75, upload_to='whatever')
    owner = models.ForeignKey(User, related_name="img", null=True, on_delete=CASCADE)

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import timezone

class ProfileModel(models.Model):
    
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name="profile", null=True, on_delete=CASCADE)
    phone_number = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description

