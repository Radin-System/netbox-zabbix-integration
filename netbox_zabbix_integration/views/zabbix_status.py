# views.py
from netbox.views import MediaView
from netbox.plugins import get_plugin_config

class ZabbixStatusView(MediaView):
    template_name = 'netbox_zabbix_integration/zabbix-status.html'

    def get(self, request, *args, **kwargs):
        # Retrieve configuration settings
        zabbix_url = get_plugin_config('netbox_zabbix_integration', 'zabbix_url')
        zabbix_token = get_plugin_config('netbox_zabbix_integration', 'zabbix_token')
        verify_ssl = get_plugin_config('netbox_zabbix_integration', 'verify_ssl')

        # Test connection (basic example)
        connection_status = "Unknown"
        error_message = None

        # Context for rendering the template
        context = {
            'zabbix_url': zabbix_url,
            'connection_status': connection_status,
            'error_message': error_message,
        }
        return self.render(request, context)
