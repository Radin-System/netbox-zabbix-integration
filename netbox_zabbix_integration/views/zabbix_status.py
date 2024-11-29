# views.py
from django.views.generic import View
from netbox.plugins import get_plugin_config
from django.shortcuts import render

class ZabbixStatusView(View):
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
        return render(request, context)
