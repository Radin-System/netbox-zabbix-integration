from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

# Choices
class RelationshipStatusChoices(ChoiceSet):
    key = 'relation_status.action'

    CHOICES = [
        ('pending', 'Pending', 'white'),
        ('created', 'Created', 'green'),
        ('synced', 'Synced', 'teal'),
        ('deleted', 'Deleted on Zabbix', 'orange'),
        ('error', 'Error', 'red'),
    ]

class ZabbixModelsChoices(ChoiceSet):
    key = 'zabbix_model.type'

    CHOICES = [
        ('host', 'Host', 'white'),
        ('hostgroup', 'Host Group', 'white'),
        ('template', 'Template', 'white'),
    ]

# Model
class Relationship(NetBoxModel):
    # Polymorphic relation fields
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        limit_choices_to={
            'model__in': ['device', 'tenant', 'site', 'platform']
        },
    )
    object_id = models.PositiveIntegerField()
    assigned_object = GenericForeignKey('content_type', 'object_id')

    zabbix_model = models.CharField(
        max_length=30,
        choices=ZabbixModelsChoices,
        blank=False,
        null=False,
    )

    zabbix_id = models.PositiveIntegerField(
        unique=True,
        blank=False,
        null=False,
    )

    zabbix_name = models.CharField(
        max_length=256,
        unique=True,
        blank=False,
        null=False,
    )

    status = models.CharField(
        max_length=30,
        choices=RelationshipStatusChoices,
        blank=False,
        null=False,
    )

    class Meta:
        db_table = 'reletionship'
        ordering = ('content_type', 'status')
        default_views = False

    def get_status_color(self):
        return RelationshipStatusChoices.colors.get(self.status)

    def get_zabbix_model_color(self):
        return ZabbixModelsChoices.colors.get(self.zabbix_model)

    def __str__(self):
        return f'{self.assigned_object} ({self.zabbix_model}) -> {self.zabbix_name}'

    def get_absolute_url(self):
        return reverse('plugins:zabbix_integration:reletionship', args=[self.pk])
