# -*- coding UTF-8 -*-

from django.db import models

class Talk(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    day = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    duration = models.CharField(max_length=20, blank=True)
    place = models.CharField(max_length=20, blank=True)
    speaker_name = models.CharField(max_length=75)
    speaker_site = models.URLField(verify_exists=False, blank=True)
    speaker_email = models.EmailField()

    def __unicode__(self):
        return "%s - %s" % (self.speaker_name, self.title)