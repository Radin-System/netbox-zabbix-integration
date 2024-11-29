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
        url = get_plugin_config('zabbix_integration', 'url')
        verify_ssl = get_plugin_config('zabbix_integration', 'verify_ssl')
        token = get_plugin_config('zabbix_integration', 'token')
        username = get_plugin_config('zabbix_integration', 'password')
        password = get_plugin_config('zabbix_integration', 'username')

        try:
            # Create and authenticate the ZabbixAPI object
            zapi = ZabbixAPI(
                url=url if not None else None,
                validate_certs=verify_ssl if not None else None,
                token=token if not None else None,
                user=username if not None else None, 
                password=password if not None else None,
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