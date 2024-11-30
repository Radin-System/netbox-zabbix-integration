from django.views.generic import View
from netbox.plugins import get_plugin_config
from django.shortcuts import render

from netbox_zabbix_integration.zabbix_api import ZabbixAPIManager

class ZabbixStatusView(View):
    template_name = 'netbox_zabbix_integration/zabbix_status.html'

    def get(self, request, *args, **kwargs):
        # Retrieve configuration settings
        url = get_plugin_config('netbox_zabbix_integration', 'url')
        verify_ssl = get_plugin_config('netbox_zabbix_integration', 'verify_ssl')
        token = get_plugin_config('netbox_zabbix_integration', 'token')
        username = get_plugin_config('netbox_zabbix_integration', 'username')
        connection_status = "Unknown"
        api_version = None
        error_message = None
        auth_mode = 'UNKHOWN'

        if token is not None:
            auth_mode = 'Token'
        elif username is not None:
            auth_mode = 'Username'

        try:
            zapi = ZabbixAPIManager.get_instance()
            api_version = str(zapi.api_version())
            connection_status = 'Online'
        except Exception as e:
            connection_status = 'Offline'
            error_message = str(e)

        # Context for rendering the template
        context = {
            'zabbix_url': url,
            'verify_ssl': verify_ssl,
            'connection_status': connection_status,
            'error_message': error_message,
            'auth_mode': auth_mode,
            'api_version': api_version,
        }
        return render(request, self.template_name, context)

__all__ = [
    'ZabbixStatusView',
]