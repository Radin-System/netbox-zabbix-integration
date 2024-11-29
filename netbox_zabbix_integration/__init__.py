from netbox.plugins import PluginConfig, register_menu_items
from netbox_zabbix_integration.plugin_hooks import add_sync_button

class NetboxZabbixIntegrationConfig(PluginConfig):
    name = 'netbox_zabbix_integration'
    verbose_name = ' Netbox Zabbix Integration'
    description = 'For Integration between Netbox and Zabbix'
    version = '1.0.0'
    base_url = 'zabbix-integration'
    author = 'radin system'
    author_email = 'info@rsto.ir'
    required_settings = []
    default_settings = {
        'INSTALLED_APPS': [
            'netbox_zabbix_integration',
        ],
    }
    caching_config = {}

config = NetboxZabbixIntegrationConfig