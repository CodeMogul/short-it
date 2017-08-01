from django.db import models
from django.conf import settings

from .utils import create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)
HOST = getattr(settings, 'HOST', 'http://127.0.0.1:8000/')

class ShortItURLManager(models.Manager):
    def all(self, *args, **kwargs):
        """
            Redefine all to filter the ouptuts if required.
        """
        qs_all = super(ShortItURLManager, self).all(*args, **kwargs)
        qs = qs_all.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = ShortItURL.objects.filter(id__gte=1)
        new_codes = 0
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]     # Order by IDs descending
        for q in qs:
            q.shortcode =create_shortcode(q)
            print("{0}:{1}".format(q.id, q.shortcode))
            q.save()
            new_codes += 1
        return "New codes generated: {0}".format(new_codes)

class ShortItURL(models.Model):
    # null = Ture   =>  Empty values in database is okay.
    # blank = True  =>  Not required in Forms/Integrity
    url         = models.CharField(max_length=200, validators=[validate_url, validate_dot_com])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)       #everytime model is saved
    timestamp   = models.DateTimeField(auto_now_add=True)   #when model is created
    active      = models.BooleanField(default=True)

    # Replace the default model Manager with Custom Model Manager
    objects = ShortItURLManager()

    # class Meta:
    #     ordering = 'url'

    def save(self, *args, **kwargs):
        if self.shortcode == None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(ShortItURL, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        return HOST + self.shortcode

# Run to create Database table
'''
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''
