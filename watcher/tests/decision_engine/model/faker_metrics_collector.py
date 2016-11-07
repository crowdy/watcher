# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
#
# Authors: Jean-Emile DARTOIS <jean-emile.dartois@b-com.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

import oslo_utils


class FakerMetricsCollector(object):
    def __init__(self):
        self.emptytype = ""

    def empty_one_metric(self, emptytype):
        self.emptytype = emptytype

    def mock_get_statistics(self, resource_id, meter_name, period,
                            aggregate='avg'):
        result = 0
        if meter_name == "hardware.cpu.util":
            result = self.get_usage_node_cpu(resource_id)
        elif meter_name == "compute.node.cpu.percent":
            result = self.get_usage_node_cpu(resource_id)
        elif meter_name == "hardware.memory.used":
            result = self.get_usage_node_ram(resource_id)
        elif meter_name == "cpu_util":
            result = self.get_average_usage_instance_cpu(resource_id)
        elif meter_name == "memory.resident":
            result = self.get_average_usage_instance_memory(resource_id)
        elif meter_name == "hardware.ipmi.node.outlet_temperature":
            result = self.get_average_outlet_temperature(resource_id)
        elif meter_name == "hardware.ipmi.node.airflow":
            result = self.get_average_airflow(resource_id)
        elif meter_name == "hardware.ipmi.node.temperature":
            result = self.get_average_inletT(resource_id)
        elif meter_name == "hardware.ipmi.node.power":
            result = self.get_average_power(resource_id)
        return result

    def mock_get_statistics_wb(self, resource_id, meter_name, period,
                               aggregate='avg'):
        result = 0
        if meter_name == "cpu_util":
            result = self.get_average_usage_instance_cpu_wb(resource_id)
        return result

    def get_average_outlet_temperature(self, uuid):
        """The average outlet temperature for host"""
        mock = {}
        mock['Node_0'] = 30
        # use a big value to make sure it exceeds threshold
        mock['Node_1'] = 100
        if uuid not in mock.keys():
            mock[uuid] = 100
        return mock[str(uuid)]

    def get_usage_node_ram(self, uuid):
        mock = {}
        # Ceilometer returns hardware.memory.used samples in KB.
        mock['Node_0'] = 7*oslo_utils.units.Ki
        mock['Node_1'] = 5*oslo_utils.units.Ki
        mock['Node_2'] = 29*oslo_utils.units.Ki
        mock['Node_3'] = 8*oslo_utils.units.Ki
        mock['Node_4'] = 4*oslo_utils.units.Ki

        if uuid not in mock.keys():
            # mock[uuid] = random.randint(1, 4)
            mock[uuid] = 8

        return float(mock[str(uuid)])

    def get_average_airflow(self, uuid):
        """The average outlet temperature for host"""
        mock = {}
        mock['Node_0'] = 400
        # use a big value to make sure it exceeds threshold
        mock['Node_1'] = 100
        if uuid not in mock.keys():
            mock[uuid] = 200
        return mock[str(uuid)]

    def get_average_inletT(self, uuid):
        """The average outlet temperature for host"""
        mock = {}
        mock['Node_0'] = 24
        mock['Node_1'] = 26
        if uuid not in mock.keys():
            mock[uuid] = 28
        return mock[str(uuid)]

    def get_average_power(self, uuid):
        """The average outlet temperature for host"""
        mock = {}
        mock['Node_0'] = 260
        mock['Node_1'] = 240
        if uuid not in mock.keys():
            mock[uuid] = 200
        return mock[str(uuid)]

    def get_usage_node_cpu(self, uuid):
        """The last VM CPU usage values to average

            :param uuid:00
            :return:
            """
        # query influxdb stream

        # compute in stream

        # Normalize
        mock = {}
        # node 0
        mock['Node_0_hostname_0'] = 7
        mock['Node_1_hostname_1'] = 7
        # node 1
        mock['Node_2_hostname_2'] = 80
        # node 2
        mock['Node_3_hostname_3'] = 5
        mock['Node_4_hostname_4'] = 5
        mock['Node_5_hostname_5'] = 10

        # node 3
        mock['Node_6_hostname_6'] = 8
        mock['Node_19_hostname_19'] = 10
        # node 4
        mock['INSTANCE_7_hostname_7'] = 4

        mock['Node_0'] = 7
        mock['Node_1'] = 5
        mock['Node_2'] = 10
        mock['Node_3'] = 4
        mock['Node_4'] = 2

        if uuid not in mock.keys():
            # mock[uuid] = random.randint(1, 4)
            mock[uuid] = 8

        return float(mock[str(uuid)])

    def get_average_usage_instance_cpu_wb(self, uuid):
        """The last VM CPU usage values to average

            :param uuid:00
            :return:
            """
        # query influxdb stream

        # compute in stream

        # Normalize
        mock = {}
        # node 0
        mock['INSTANCE_1'] = 80
        mock['73b09e16-35b7-4922-804e-e8f5d9b740fc'] = 50
        # node 1
        mock['INSTANCE_3'] = 20
        mock['INSTANCE_4'] = 10
        return float(mock[str(uuid)])

    def get_average_usage_instance_cpu(self, uuid):
        """The last VM CPU usage values to average

        :param uuid:00
        :return:
        """
        # query influxdb stream

        # compute in stream

        # Normalize
        mock = {}
        # node 0
        mock['INSTANCE_0'] = 7
        mock['INSTANCE_1'] = 7
        # node 1
        mock['INSTANCE_2'] = 10
        # node 2
        mock['INSTANCE_3'] = 5
        mock['INSTANCE_4'] = 5
        mock['INSTANCE_5'] = 10

        # node 3
        mock['INSTANCE_6'] = 8

        # node 4
        mock['INSTANCE_7'] = 4
        if uuid not in mock.keys():
            # mock[uuid] = random.randint(1, 4)
            mock[uuid] = 8

        return mock[str(uuid)]

    def get_average_usage_instance_memory(self, uuid):
        mock = {}
        # node 0
        mock['INSTANCE_0'] = 2
        mock['INSTANCE_1'] = 5
        # node 1
        mock['INSTANCE_2'] = 5
        # node 2
        mock['INSTANCE_3'] = 8
        mock['INSTANCE_4'] = 5
        mock['INSTANCE_5'] = 16

        # node 3
        mock['INSTANCE_6'] = 8

        # node 4
        mock['INSTANCE_7'] = 4
        if uuid not in mock.keys():
            # mock[uuid] = random.randint(1, 4)
            mock[uuid] = 10

        return mock[str(uuid)]

    def get_average_usage_instance_disk(self, uuid):
        mock = {}
        # node 0
        mock['INSTANCE_0'] = 2
        mock['INSTANCE_1'] = 2
        # node 1
        mock['INSTANCE_2'] = 2
        # node 2
        mock['INSTANCE_3'] = 10
        mock['INSTANCE_4'] = 15
        mock['INSTANCE_5'] = 20

        # node 3
        mock['INSTANCE_6'] = 8

        # node 4
        mock['INSTANCE_7'] = 4

        if uuid not in mock.keys():
            # mock[uuid] = random.randint(1, 4)
            mock[uuid] = 4

        return mock[str(uuid)]

    def get_virtual_machine_capacity(self, instance_uuid):
        return random.randint(1, 4)
