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

from haproxy_manager.manager import Manager

import os
import glob
import unittest


class ManagerTest(unittest.TestCase):

    def setUp(self):
        self.manager = Manager('tests/output/')
        self.template_val = self.manager.get("frontend-machine0001")

    def tearDown(self):
        filelist = glob.glob("*.cfg")
        for f in filelist:
            os.remove(f)

    def test_list(self):
        file_list = [
            {"name": "frontend-machine0001"},
            {"name": "global"},
            {"name": "backend-machine0001"},
        ]
        self.assertEqual(self.manager.list(), file_list)

    def test_get(self):
        name = "frontend-machine0001"
        self.assertNotEqual(len(self.manager.get(name)), 0)

    def test_get_empty_value_for_nonexistant_config(self):
        name = "frontend-invalid0001"
        self.assertEqual(self.manager.get(name), {})
