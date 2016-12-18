from django.db import models
from django.utils import timezone


class addServer(models.Model):
    user = models.ForeignKey('auth.User')
    server = models.CharField(max_length=200)
    details = models.TextField()
    ipAddress = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def creation(self):
        self.created_date = timezone.now()
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.server

class serverList(models.Model):
    hosts = []
    def listCrt(self):  
        posts = addServer.objects.order_by('created_date')
        for servers in posts:
            host = servers.ipAddress
            self.hosts.append(host)
        return hosts