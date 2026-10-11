"""
API URL patterns for NetBox Backup Ops Plugin.

For more information on NetBox REST API routing, see:
https://docs.netbox.dev/en/stable/plugins/development/rest-api/#routers

For Django REST Framework routers, see:
https://www.django-rest-framework.org/api-guide/routers/
"""

from netbox.api.routers import NetBoxRouter

from .views import BackupopsViewSet

app_name = "netbox_backup_ops"

router = NetBoxRouter()
router.register("backup-opss", BackupopsViewSet)

urlpatterns = router.urls

