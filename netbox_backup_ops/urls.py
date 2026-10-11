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
    path("backup-opss/", views.BackupopsListView.as_view(), name="backupops_list"),
    path("backup-opss/add/", views.BackupopsEditView.as_view(), name="backupops_add"),
    path("backup-opss/<int:pk>/", views.BackupopsView.as_view(), name="backupops"),
    path("backup-opss/<int:pk>/edit/", views.BackupopsEditView.as_view(), name="backupops_edit"),
    path("backup-opss/<int:pk>/delete/", views.BackupopsDeleteView.as_view(), name="backupops_delete"),
    path(
        "backup-opss/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="backupops_changelog",
        kwargs={"model": models.Backupops},
    ),
)
