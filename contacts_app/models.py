from django.db import models
import logging

logger = logging.getLogger('contacts_model')

class Report(models.Model):
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    is_report = models.BooleanField(blank=True)
    bug_type = models.CharField(max_length=20, blank=True)
    date = models.DateField(auto_now=True)



    def __text__(self):
        return self.text

    def __title__(self):
        return self.title



