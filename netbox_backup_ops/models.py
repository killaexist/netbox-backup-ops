"""
Models for NetBox Backup Ops Plugin.

For more information on NetBox models, see:
https://docs.netbox.dev/en/stable/plugins/development/models/

For NetBox model features (tags, custom fields, change logging, etc.), see:
https://docs.netbox.dev/en/stable/development/models/#netbox-model-features
"""

from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class Backupops(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = "netbox_backup_ops"
        ordering = ("name",)
        verbose_name_plural = "Backupopss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_backup_ops:backupops", args=[self.pk])
