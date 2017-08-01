from django.db import models

from shortner.models import ShortItURL

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortItURL):
            obj, created = self.get_or_create(shortit_url = instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None
    
class ClickEvent(models.Model):
    shortit_url = models.OneToOneField(ShortItURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)       #everytime model is saved
    timestamp   = models.DateTimeField(auto_now_add=True)   #when model is created

    objects     = ClickEventManager()

    def __str__(self):
        return "Clicked {0} times.".format(self.count)
