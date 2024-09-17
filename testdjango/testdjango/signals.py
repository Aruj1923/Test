import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading
from djtest.models import Profile


# @receiver(post_save, sender=User)
# def slow_handler(sender, instance, **kwargs):
#     print("Signal received! Processing...")
#     time.sleep(5)  # Simulate slow operation
#     print("Signal processing completed.")

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    print("Signal: Creating profile...")
    # Create a profile for the user
    
    Profile.objects.create(user=instance)
    print("Signal: Profile created.")