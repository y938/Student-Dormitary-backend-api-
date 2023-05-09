from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
import random
import string

User = get_user_model()

@receiver(post_save, sender=User)
def send_user_info(sender, instance, created, **kwargs):
    if created:
        # Generate a random password
        password = "#123@abc"
        validate_password(password)

        # Update the user's password
        instance.set_password(password)
        instance.save()

        # Send the password via email
        subject = "Account Information"
        message = f"Your Dorm Account created Sucessfully.\n\n username: {instance.username}\nYour password: {password} \n\n Please don't share your password with friends!"
        from_email = "noreply@AASTUDormitary.com"
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
