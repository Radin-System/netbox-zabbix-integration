from netbox.plugins import PluginConfig

class NetboxZabbixIntegrationConfig(PluginConfig):
    name = 'netbox_zabbix_integration'
    verbose_name = ' Netbox Zabbix Integration'
    description = 'For Integration between Netbox and Zabbix'
    version = '1.0.0'
    base_url = 'netbox-zabbix-integration'
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