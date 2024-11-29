from zabbix_utils import ZabbixAPI
from netbox.plugins import get_plugin_config
import logging

logger = logging.getLogger('netbox.plugins.zabbix_integration')

class ZabbixAPIManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        """Retrieve the singleton instance of ZabbixAPI."""
        if cls._instance is None:
            cls._instance = cls._create_instance()
        return cls._instance

    @classmethod
    def _create_instance(cls):
        """Create a new ZabbixAPI instance and authenticate."""
        # Get plugin configuration
        url = get_plugin_config('netbox_zabbix_integration', 'url')
        verify_ssl = get_plugin_config('netbox_zabbix_integration', 'verify_ssl')
        token = get_plugin_config('netbox_zabbix_integration', 'token')
        username = get_plugin_config('netbox_zabbix_integration', 'password')
        password = get_plugin_config('netbox_zabbix_integration', 'username')

        try:
            # Create and authenticate the ZabbixAPI object
            if token:
                zapi = ZabbixAPI(
                    url=url,
                    validate_certs=verify_ssl,
                    token=token,
                    timeout=10,
                    )
            else:
                zapi = ZabbixAPI(
                    url=url,
                    validate_certs=verify_ssl,
                    user=username,
                    password=password,
                    timeout=10,
                    )

            logger.info("Successfully connected to Zabbix API.")
            return zapi
        except Exception as e:
            logger.error(f"Failed to connect to Zabbix API: {e}")
            raise

    @classmethod
    def reset_instance(cls):
        """Reset the ZabbixAPI instance (e.g., after configuration changes)."""
        cls._instance = None