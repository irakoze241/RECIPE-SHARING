import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipeshare.settings')
django.setup()
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@recipeshare.com', 'admin1234')
    print('Superuser created: admin / admin1234')
else:
    print('Superuser already exists.')
