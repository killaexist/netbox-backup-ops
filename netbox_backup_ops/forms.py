"""
Forms for NetBox Backup Ops Plugin.

For more information on NetBox forms, see:
https://docs.netbox.dev/en/stable/plugins/development/forms/
"""

from netbox.forms import NetBoxModelForm

from .models import Backupops


class BackupopsForm(NetBoxModelForm):
    class Meta:
        model = Backupops
        fields = ("name", "tags")
