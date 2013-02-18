# Copyright 2013 Locaweb.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# @author: Willian Molinari (PotHix), Locaweb.

from haproxy_manager.haproxy_config import HaproxyConfig

import unittest


class ConfigWriterTest(unittest.TestCase):

    def setUp(self):
        self.clazz = HaproxyConfig('tests/output/')

    def test_concat(self):
        config = "machine0001c\n\nmachine0002c\n\nmachine0003c\n"
        self.assertEqual(self.clazz.concat(), config)

    def test_write(self):
        config = "machine0001c\n\nmachine0002c\n\nmachine0003c\n"
        self.clazz.write(self.clazz.concat())
        self.assertEqual(open("tests/output/haproxy.cfg").read(), config)
