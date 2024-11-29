from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_zabbix_integration:zabbix-status',
        link_text='Zabbix Status',
        staff_only=True,
    ),
    PluginMenuItem(
        link='plugins:netbox_zabbix_integration:relationship_list',
        link_text='Relationships',
        staff_only=True,
    ),
)