"""
Navigation menu items for NetBox Backup Ops Plugin.

For more information on navigation menus, see:
https://docs.netbox.dev/en/stable/plugins/development/navigation/
"""

from netbox.plugins import PluginMenuButton, PluginMenuItem

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_backup_ops:backupops_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_backup_ops:backupops_list",
        link_text="Backup Ops",
        buttons=plugin_buttons,
    ),
)
