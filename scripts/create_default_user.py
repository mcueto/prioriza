import os
from django.contrib.auth.models import User


def run():
    try:
        if 'DEFAULT_USER_USERNAME' in os.environ and 'DEFAULT_USER_PASSWORD' in os.environ and 'DEFAULT_USER_EMAIL' in os.environ:
            user = User.objects.create_user(
                os.environ.get('DEFAULT_USER_USERNAME'),
                password=os.environ.get('DEFAULT_USER_PASSWORD'),
                email=os.environ.get('DEFAULT_USER_EMAIL')
            )

            user.is_superuser = True
            user.is_staff = True
            user.save()

    except Exception as e:
        pass
