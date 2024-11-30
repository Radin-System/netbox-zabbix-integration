from netbox.plugins import PluginTemplateExtension

class DeviceSyncButton(PluginTemplateExtension):
    model = "dcim.device"

    def right_page(self):
        return self.render("netbox_zabbix_integration/misc/device_button.html")


template_extensions = [DeviceSyncButton]
