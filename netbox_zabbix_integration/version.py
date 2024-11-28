from netbox.plugins import PluginConfig

class NetboxZabbixIntegrationConfig(PluginConfig):
    name = 'netbox_zabbix_integration'
    verbose_name = ' Metbox Zabbix Integration'
    description = 'For Integration between Netbox and Zabbix'
    version = '1.0.0'
    base_url = 'zabbix-integration'

config = NetboxZabbixIntegrationConfig