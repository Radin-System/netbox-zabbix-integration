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
    object_id = models.PositiveIntegerField(
        verbose_name='Object ID',
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        limit_choices_to={
            'model__in': ['device', 'tenant', 'site', 'platform']
        },
    )

    assigned_object = GenericForeignKey(
        'content_type',
        'object_id',
    )
    assigned_object.verbose_name = 'Assigned Object'

    zabbix_id = models.PositiveIntegerField(
        verbose_name='Zabbix ID',
        unique=True,
        blank=False,
        null=False,
    )

    zabbix_model = models.CharField(
        verbose_name='Zabbix Model',
        max_length=30,
        choices=ZabbixModelsChoices,
        blank=False,
        null=False,
    )

    zabbix_object = models.CharField(
        verbose_name='Zabbix Object',
        max_length=256,
        unique=True,
        blank=False,
        null=False,
    )

    status = models.CharField(
        verbose_name='Status',
        max_length=30,
        choices=RelationshipStatusChoices,
        blank=False,
        null=False,
    )

    class Meta:
        db_table = 'relationship'
        ordering = ('content_type',)

    def get_status_color(self):
        return RelationshipStatusChoices.colors.get(self.status)

    def get_zabbix_model_color(self):
        return ZabbixModelsChoices.colors.get(self.zabbix_model)

    def __str__(self):
        return f'{self.assigned_object} ({self.zabbix_model}) -> {self.zabbix_object}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_zabbix_integration:relationship', args=[self.pk])

__all__ = [
    'Relationship',
]