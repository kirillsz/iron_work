
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

class Profile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    phone       = models.CharField(max_length=30, blank=True, verbose_name="Телефон")
    created     = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return str(self.user)

@receiver(post_delete, sender=Profile)
def profile_user_delete(sender, instance, **kwargs):

    try:
        instance.user.delete()
    except ObjectDoesNotExist:
        pass

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

