from netbox.views import generic
from . import models, tables

# views.py
from django.views.generic import TemplateView
from netbox.plugins import get_plugin_config
import requests

class ZabbixStatusView(TemplateView):
    template_name = "zabbix_integration/status.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get plugin configuration
        zabbix_url = get_plugin_config('zabbix_integration', 'zabbix_url')
        zabbix_token = get_plugin_config('zabbix_integration', 'zabbix_token')
        verify_ssl = get_plugin_config('zabbix_integration', 'verify_ssl')

        # Initialize status details
        connection_status = "Unknown"
        error_message = None

        # Test connection to Zabbix
        if zabbix_url and zabbix_token:
            try:
                response = requests.get(zabbix_url, verify=verify_ssl, timeout=5)
                if response.status_code == 200:
                    connection_status = "Connected"
                else:
                    connection_status = "Failed"
                    error_message = f"HTTP {response.status_code}"
            except requests.RequestException as e:
                connection_status = "Failed"
                error_message = str(e)
        else:
            connection_status = "Not Configured"
            error_message = "Missing URL or token."

        # Populate context
        context.update({
            "zabbix_url": zabbix_url,
            "connection_status": connection_status,
            "error_message": error_message,
        })
        return context

class RelationshipView(generic.ObjectView):
    queryset = models.Relationship.objects.all()

class RelationshipListView(generic.ObjectListView):
    queryset = models.Relationship.objects.all()
    table = tables.RelationshipTable
