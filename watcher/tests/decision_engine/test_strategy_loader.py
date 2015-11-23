# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
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

from __future__ import unicode_literals

from mock import patch
from stevedore.extension import Extension
from stevedore.extension import ExtensionManager
from watcher.decision_engine.framework.strategy.strategy_loader import \
    StrategyLoader
from watcher.decision_engine.strategies.dummy_strategy import DummyStrategy
from watcher.tests import base


class TestLoader(base.BaseTestCase):

    @patch("watcher.decision_engine.framework.strategy."
           "strategy_loader.ExtensionManager")
    def test_strategy_loader(self, m_extension_manager):
        dummy_strategy_name = "dummy"
        m_extension_manager.return_value = ExtensionManager.make_test_instance(
            extensions=[Extension(
                name=dummy_strategy_name,
                entry_point="%s:%s" % (DummyStrategy.__module__,
                                       DummyStrategy.__name__),
                plugin=DummyStrategy,
                obj=None,
            )],
            namespace="watcher_strategies",
        )
        # Set up the fake Stevedore extensions
        strategy_loader = StrategyLoader()
        loaded_strategy = strategy_loader.load("dummy")

        self.assertEqual("dummy", loaded_strategy.name)
        self.assertEqual("Dummy Strategy", loaded_strategy.description)
