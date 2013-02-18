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
from haproxy_manager.config_files import ConfigFiles

import os
import glob
import unittest

DEFAULT_TEST_ARGS = {"name": "machine0001", "type": "frontend", "args":{"maxconn":1}}


class ManagerTest(unittest.TestCase):

    def setUp(self):
        self.test_path = 'tests/output/'
        self.manager = Manager(self.test_path)

        self.config_files = ConfigFiles(self.test_path)
        self.config_files.global_writer(DEFAULT_TEST_ARGS)
        self.config_files.backend_writer(DEFAULT_TEST_ARGS)
        self.config_files.frontend_writer(DEFAULT_TEST_ARGS)

    def tearDown(self):
        filelist = glob.glob(self.test_path + "/*.cfg")
        for f in filelist:
            os.remove(f)

    def test_list(self):
        file_list = [
            {"name": "machine0001"},
        ]
        self.assertEqual(self.manager.list("frontend"), file_list)

    def test_get(self):
        ftype, fname = "frontend", "machine0001"
        self.config_files.frontend_writer(DEFAULT_TEST_ARGS)
        self.assertNotEqual(len(self.manager.get(ftype, fname)), 0)

    def test_get_empty_value_for_nonexistant_config(self):
        ftype, fname = "frontend", "invalid0001"
        self.assertEqual(self.manager.get(ftype, fname), {})

    def test_delete(self):
        ftype, fname = "frontend", "machine0001"
        self.config_files.frontend_writer(DEFAULT_TEST_ARGS)
        self.manager.delete(ftype, fname)

    def test_update(self):
        ftype, fname = "frontend", "machine0001"
        self.manager.update(ftype, fname, {"mode": "udp"})
