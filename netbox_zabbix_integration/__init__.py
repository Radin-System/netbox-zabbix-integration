from django.core.exceptions import ImproperlyConfigured
from netbox.plugins import PluginConfig, get_plugin_config

from .validation import validate_url, validate_authentication, validate_bool
from .extensions import DeviceSyncButton

class NetboxZabbixIntegrationConfig(PluginConfig):
    name = 'netbox_zabbix_integration'
    verbose_name = 'Zabbix Integration'
    description = 'For Integration between Netbox and Zabbix'
    author = 'radin system'
    author_email = 'info@rsto.ir'
    version = '1.0.0'

    base_url = 'zabbix-integration'

    required_settings = []
    default_settings = {
        'url': None,
        'verify_ssl': None,
        'token': None,
        'username': None,
        'password': None,
    }
    caching_config = {}
    template_extensions = [DeviceSyncButton,]

    def ready(self):
        super().ready()

        # Validate configuration
        self.validate_configuration()

    def validate_configuration(self):
        # Get plugin settings
        url: str = get_plugin_config(self.name, 'url')
        verify_ssl: bool = get_plugin_config(self.name, 'verify_ssl')
        token: str = get_plugin_config(self.name, 'token')
        username: str = get_plugin_config(self.name, 'username')
        password: str = get_plugin_config(self.name, 'password')

        # Validate zabbix_url
        if not validate_url(url):
            raise ImproperlyConfigured(f"Invalid Zabbix URL '{url}'. Check the configuration")

        # Validate zabbix_token
        if not validate_authentication(token, username, password):
            raise ImproperlyConfigured("Invalid Zabbix Authentication Method. Check the configuration")

        if not validate_bool(verify_ssl):
            raise ImproperlyConfigured("Parameter 'verify_ssl' Must Be Instance of Type Boolean. Check the configuration")

config = NetboxZabbixIntegrationConfig