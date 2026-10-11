"""
Views for NetBox Backup Ops Plugin.

For more information on NetBox views, see:
https://docs.netbox.dev/en/stable/plugins/development/views/

For generic view classes, see:
https://docs.netbox.dev/en/stable/development/views/
"""

from netbox.views import generic

from . import filtersets, forms, models, tables


class BackupopsView(generic.ObjectView):
    queryset = models.Backupops.objects.all()


class BackupopsListView(generic.ObjectListView):
    queryset = models.Backupops.objects.all()
    table = tables.BackupopsTable
    filterset = filtersets.BackupopsFilterSet


class BackupopsEditView(generic.ObjectEditView):
    queryset = models.Backupops.objects.all()
    form = forms.BackupopsForm


class BackupopsDeleteView(generic.ObjectDeleteView):
    queryset = models.Backupops.objects.all()
