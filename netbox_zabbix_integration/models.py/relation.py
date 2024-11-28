from django.contrib.postgres.fields import ArrayField
from django.db import models

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class RelationshipStatusChoices(ChoiceSet):
    key = 'RelationStatus.action'

    CHOICES = [
        ('pending', 'Pending', 'white'),
        ('created', 'Created', 'green'),
        ('synced', 'Synced', 'teal'),
        ('deleted', 'Deleted on Zabbix', 'orange'),
        ('error', 'Error', 'red'),
    ]

class ZabbixRelationship(NetBoxModel):
    class Meta:
        ordering = ('object','status')

    object = models.ForeignKey(
        to='dcim.device',
        on_delete=models.PROTECT,
        unique=True,
        related_name='zabbix_host',
        blank=False,
        null=False,
    )

    zabbix_id = models.PositiveIntegerField(
        unique=True,
        blank=False,
        null=False,
    )

    status = models.CharField(
        max_length=30,
        choices=RelationshipStatusChoices
    )

    def get_status_color(self):
        return RelationshipStatusChoices.colors.get(self.status)

    def __str__(self) -> str:
        return f'{self.object}'
