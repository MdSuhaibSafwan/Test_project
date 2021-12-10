from django.contrib.auth.models import User
from .models import Content, UserProfile, UserVerificationOTp
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

#post save, presave, postdelete, predelete


@receiver(signal=post_save, sender=Content)   # sender, instance, created, **kwargs
def validate_title_for_content(sender, instance, created, **kwargs):
    # print("Inside signals of content")
    # print(sender, instance, created)

    if created == True:
        user = instance.user
        qs = user.content_set.filter(title=instance.title)
        if qs.count() > 1:
            instance.delete()
            raise ValueError("TItle already exist for this user")
        else:
            print("Checked successfully and nothing found")



@receiver(signal=post_save, sender=User)
def send_mail_to_user(sender, instance, created, **kwargs):
    if created:
        token_obj = UserVerificationOTp.objects.create(user=instance)
        print(token_obj)
        send_mail(
            subject="sending_token",
            message=f"http://127.0.0.1:8000/verify/{token_obj.token}/",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email],
        )


@receiver(signal=post_save, sender=User)
def send_mail_to_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)