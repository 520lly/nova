#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.notifications.objects import base
from nova.objects import base as nova_base
from nova.objects import fields


@nova_base.NovaObjectRegistry.register_notification
class AggregatePayload(base.NotificationPayloadBase):
    SCHEMA = {
        'id': ('aggregate', 'id'),
        'uuid': ('aggregate', 'uuid'),
        'name': ('aggregate', 'name'),
        'hosts': ('aggregate', 'hosts'),
        'metadata': ('aggregate', 'metadata'),
    }
    # Version 1.0: Initial version
    VERSION = '1.0'
    fields = {
        'id': fields.IntegerField(),
        'uuid': fields.UUIDField(nullable=False),
        'name': fields.StringField(),
        'hosts': fields.ListOfStringsField(nullable=True),
        'metadata': fields.DictOfStringsField(nullable=True),
    }

    def __init__(self, aggregate, **kwargs):
        super(AggregatePayload, self).__init__(**kwargs)
        self.populate_schema(aggregate=aggregate)


@base.notification_sample('aggregate-create-start.json')
@base.notification_sample('aggregate-create-end.json')
@base.notification_sample('aggregate-delete-start.json')
@base.notification_sample('aggregate-delete-end.json')
@nova_base.NovaObjectRegistry.register_notification
class AggregateNotification(base.NotificationBase):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'payload': fields.ObjectField('AggregatePayload')
    }
