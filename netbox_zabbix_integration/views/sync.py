from django.views.generic import View
from netbox.plugins import get_plugin_config
from django.shortcuts import render

from netbox_zabbix_integration.zabbix_api import ZabbixAPIManager

class ObjectSyncView(View):
    template_name = 'netbox_zabbix_integration/object_sync.html'

    def get(self, request, *args, **kwargs):
        error_message = None
        model = kwargs.get('model', None)
        id = kwargs.get('id', None)

        ## Model inputs: ['tenant', 'site', 'device', 'platform']
        if model and id:
            if model == 'tenant':
                ...
            elif model == 'site':
                ...
            elif model == 'device':
                ...
            elif model == 'platform':
                ...
            else:
                raise Exception('401')

            try:
                zapi = ZabbixAPIManager.get_instance()
            except Exception as e:
                error_message = str(e)

        context = {
            'error_message': error_message,
        }
        return render(request, self.template_name, context)

__all__ = [
    'ObjectSyncView',
]