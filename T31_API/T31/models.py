from django.db import models
from django.utils.timezone import now

class Click(models.Model):
    ip_address = models.GenericIPAddressField()
    browser_info = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=now)
    project = models.CharField(max_length=100, null=True, blank=True)
    thank_you_page = models.URLField()

    def __str__(self):
        return f"Click IP:|{self.ip_address}| Time:|{self.timestamp}| Origin:|{self.project}|"

