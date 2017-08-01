import random, string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def code_generator(url='', size=SHORTCODE_MIN):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(instance.url, size)
    # importing instance class would cause cyclic import error
    model_class = instance.__class__
    qs_exists = model_class.objects.filter(shortcode=new_code).exists()
    while qs_exists:
        new_code = code_generator(instance.url, size)
        qs_exists = model_class.objects.filter(shortcode=new_code).exists()
    return new_code