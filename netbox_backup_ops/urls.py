"""
URL patterns for NetBox Backup Ops Plugin.

For more information on URL routing, see:
https://docs.netbox.dev/en/stable/plugins/development/views/#url-registration

For Django URL patterns, see:
https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (
    path("backup-ops/", views.BackupopsListView.as_view(), name="backupops_list"),
    path("backup-ops/add/", views.BackupopsEditView.as_view(), name="backupops_add"),
    path("backup-ops/<int:pk>/", views.BackupopsView.as_view(), name="backupops"),
    path("backup-ops/<int:pk>/edit/", views.BackupopsEditView.as_view(), name="backupops_edit"),
    path("backup-ops/<int:pk>/delete/", views.BackupopsDeleteView.as_view(), name="backupops_delete"),
    path(
        "backup-ops/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="backupops_changelog",
        kwargs={"model": models.Backupops},
    ),
)
