from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_zabbix_integration:zabbix_relationship_list',
        link_text='Zabbix Reletionship',
        staff_only=True,
    ),
)