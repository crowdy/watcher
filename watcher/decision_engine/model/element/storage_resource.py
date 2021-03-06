# -*- encoding: utf-8 -*-
# Copyright 2017 NEC Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc

import six

from watcher.decision_engine.model.element import base
from watcher.objects import fields as wfields


@six.add_metaclass(abc.ABCMeta)
class StorageResource(base.Element):

    VERSION = '1.0'

    fields = {
        "uuid": wfields.StringField(default=""),
        "human_id": wfields.StringField(default=""),
    }
