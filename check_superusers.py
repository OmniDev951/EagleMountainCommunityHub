import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EMCommunityProj.settings')
django.setup()

from django.contrib.auth.models import User

superusers = User.objects.filter(is_superuser=True)
print(f"Number of superusers: {superusers.count()}")
for user in superusers:
    print(f"  - {user.username}")
