"""
Test cases for NetBox Backup Ops Plugin views.
"""

from django.urls import reverse

from ..models import Backupops
from ..testing import PluginViewTestCase
from ..testing.utils import disable_warnings, get_random_string


class BackupopsViewTestCase(PluginViewTestCase):
    """Test Backupops views."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        Backupops.objects.create(name="View Test 1")
        Backupops.objects.create(name="View Test 2")
        Backupops.objects.create(name="View Test 3")

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.base_url = "plugins:netbox_backup_ops:backupops"

    def test_list_backupopss(self):
        """Test Backupops list view."""
        self.add_permissions("netbox_backup_ops.view_backupops")

        url = reverse("plugins:netbox_backup_ops:backupops_list")
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)

    def test_list_backupopss_without_permission(self):
        """Test Backupops list view without permission."""
        url = reverse("plugins:netbox_backup_ops:backupops_list")

        with disable_warnings("django.request"):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)

    def test_view_backupops(self):
        """Test Backupops detail view."""
        self.add_permissions("netbox_backup_ops.view_backupops")

        instance = Backupops.objects.first()
        url = reverse("plugins:netbox_backup_ops:backupops", kwargs={"pk": instance.pk})
        response = self.client.get(url)

        self.assertHttpStatus(response, 200)
        self.assertEqual(response.context["object"], instance)

    def test_create_backupops(self):
        """Test creating a Backupops via form."""
        self.add_permissions("netbox_backup_ops.add_backupops", "netbox_backup_ops.view_backupops")

        url = reverse("plugins:netbox_backup_ops:backupops_add")
        name = f"Created {get_random_string(10)}"

        form_data = self.post_data(
            {
                "name": name,
            }
        )

        response = self.client.post(url, form_data, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was created
        instance = Backupops.objects.get(name=name)
        self.assertEqual(instance.name, name)

    def test_create_backupops_without_permission(self):
        """Test creating a Backupops without permission."""
        url = reverse("plugins:netbox_backup_ops:backupops_add")

        with disable_warnings("django.request"):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)

    def test_edit_backupops(self):
        """Test editing a Backupops via form."""
        self.add_permissions("netbox_backup_ops.change_backupops", "netbox_backup_ops.view_backupops")

        instance = Backupops.objects.first()
        url = reverse("plugins:netbox_backup_ops:backupops_edit", kwargs={"pk": instance.pk})

        new_name = f"Edited {get_random_string(10)}"
        form_data = self.post_data(
            {
                "name": new_name,
            }
        )

        response = self.client.post(url, form_data, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was updated
        instance.refresh_from_db()
        self.assertEqual(instance.name, new_name)

    def test_delete_backupops(self):
        """Test deleting a Backupops."""
        self.add_permissions("netbox_backup_ops.delete_backupops", "netbox_backup_ops.view_backupops")

        instance = Backupops.objects.first()
        url = reverse("plugins:netbox_backup_ops:backupops_delete", kwargs={"pk": instance.pk})

        # Confirm deletion
        response = self.client.post(url, {"confirm": True}, follow=True)
        self.assertHttpStatus(response, 200)

        # Verify object was deleted
        self.assertFalse(Backupops.objects.filter(pk=instance.pk).exists())

    def test_delete_backupops_without_permission(self):
        """Test deleting a Backupops without permission."""
        instance = Backupops.objects.first()
        url = reverse("plugins:netbox_backup_ops:backupops_delete", kwargs={"pk": instance.pk})

        with disable_warnings("django.request"):
            response = self.client.get(url)
            self.assertHttpStatus(response, 403)


class BackupopsFormTestCase(PluginViewTestCase):
    """Test Backupops form validation."""

    def setUp(self):
        """Set up each test."""
        super().setUp()
        self.add_permissions("netbox_backup_ops.add_backupops", "netbox_backup_ops.view_backupops")

    def test_form_validation_empty_name(self):
        """Test form validation with empty name."""
        url = reverse("plugins:netbox_backup_ops:backupops_add")
        form_data = self.post_data({"name": ""})

        response = self.client.post(url, form_data)
        self.assertHttpStatus(response, 200)  # Form redisplay

        # Should not create object
        self.assertEqual(Backupops.objects.filter(name="").count(), 0)

    def test_form_validation_duplicate_name(self):
        """Test form validation with duplicate name."""
        Backupops.objects.create(name="Duplicate")

        url = reverse("plugins:netbox_backup_ops:backupops_add")
        form_data = self.post_data({"name": "Duplicate"})

        response = self.client.post(url, form_data)
        self.assertHttpStatus(response, 200)  # Form redisplay

        # Should only have one instance with this name
        self.assertEqual(Backupops.objects.filter(name="Duplicate").count(), 1)
