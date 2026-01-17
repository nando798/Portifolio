import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
try:
    django.setup()
    from django.template.loader import get_template
    try:
        t = get_template('home.html')
        print('FOUND', getattr(t, 'origin', None))
    except Exception as e:
        import traceback
        traceback.print_exc()
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
