"""
NetBox Backup Ops Plugin

Plugin configuration for NetBox Backup Ops Plugin.

For a complete list of PluginConfig attributes, see:
https://docs.netbox.dev/en/stable/plugins/development/#pluginconfig-attributes
"""

__author__ = """Alexandr Lakhnenko"""
__email__ = "sashaolegovitchz564@gmail.com"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class BackupopsConfig(PluginConfig):
    name = "netbox_backup_ops"
    verbose_name = "NetBox Backup Ops Plugin"
    description = "Netbox plugin for Planning & Journal in Backup System"
    author = "Alexandr Lakhnenko"
    author_email = "sashaolegovitchz564@gmail.com"
    version = __version__
    base_url = "netbox_backup_ops"
    min_version = "4.5.0"
    max_version = "4.5.99"


config = BackupopsConfig
