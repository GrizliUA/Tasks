from django.db import models

class Click(models.Model):
    ip_address = models.GenericIPAddressField()
    browser_info = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=100, null=True, blank=True)
    thank_you_page = models.URLField()

    def __str__(self):
        return f"Click IP:|{self.ip_address}| Time:|{self.timestamp}| Origin:|{self.project}|"

