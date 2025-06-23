from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.db.models.signals import post_init, post_save, pre_delete, pre_save, post_delete, pre_init
from django.core.signals import request_finished, request_started, got_request_exception

"""def login_success(sender, request, user, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"User {user.username} logged in successfully.")
    print(f"Request: {request}")
    print(f"Sender: {sender}")
    print(f"User: {user}")
    print(f"User ID: {user.id}")
    print(f"User email: {user.email}")
    print(f"Request method: {request.method}")
    print(f"Request path: {request.path}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
user_logged_in.connect(login_success, sender=User)"""

#with decorator
from django.dispatch import receiver
@receiver(user_logged_in, sender=User)
def login_success_decorator(sender, request, user, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"User {user.username} logged in successfully (decorator).")
    print(f"Request: {request}")
    print(f"Sender: {sender}")
    print(f"User: {user}")
    print(f"User ID: {user.id}")
    print(f"User email: {user.email}")
    print(f"Request method: {request.method}")
    print(f"Request path: {request.path}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
    
# logout signal
@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"User {user.username} logged out successfully.")
    print(f"Request: {request}")
    print(f"Sender: {sender}")
    print(f"User: {user}")
    print(f"User ID: {user.id}")
    print(f"User email: {user.email}")
    print(f"Request method: {request.method}")
    print(f"Request path: {request.path}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
# login failed signal
@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("----------------------------------------------------------------------")
    print("Login failed.")
    print(f"Credentials: {credentials}")
    print(f"Request: {request}")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
# Model signals
@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"Pre-save signal for User model: {instance.username}")
    print(f"Instance: {instance}")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        print("----------------------------------------------------------------------")
        print(f"User {instance.username} created successfully.")
        print(f"Instance: {instance}")
        print(f"Sender: {sender}")
        print(f"Created: {created}")
        print(f"Additional kwargs: {kwargs}")
        print("----------------------------------------------------------------------")
    else:
        print("----------------------------------------------------------------------")
        print(f"User {instance.username} updated successfully.")
        print(f"Instance: {instance}")
        print(f"Sender: {sender}")
        print(f"Created: {created}")
        print(f"Additional kwargs: {kwargs}")
        print("----------------------------------------------------------------------")
        
@receiver(post_delete, sender=User)
def post_delete_user(sender, instance, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"User {instance.username} deleted successfully.")
    print(f"Instance: {instance}")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")

@receiver(pre_delete, sender=User)
def pre_delete_user(sender, instance, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"Pre-delete signal for User model: {instance.username}")
    print(f"Instance: {instance}")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
@receiver(post_init, sender=User)
def post_init_user(sender, instance, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"Post-init signal for User model: {instance.username}")
    print(f"Instance: {instance}")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
@receiver(pre_init, sender=User)
def pre_init_user(sender, *args, **kwargs):
    print("----------------------------------------------------------------------")
    print(f"Pre-init signal for User model.")
    print(f"Sender: {sender}")
    print(f"Args: {args}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
@receiver(request_started)
def request_started_handler(sender, **kwargs):
    print("----------------------------------------------------------------------")
    print("Request started.")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
@receiver(request_finished)
def request_finished_handler(sender, **kwargs):
    print("----------------------------------------------------------------------")
    print("Request finished.")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    
@receiver(got_request_exception)
def got_request_exception_handler(sender, request, **kwargs):
    print("----------------------------------------------------------------------")
    print("Got request exception.")
    print(f"Request: {request}")
    print(f"Sender: {sender}")
    print(f"Additional kwargs: {kwargs}")
    print("----------------------------------------------------------------------")
    