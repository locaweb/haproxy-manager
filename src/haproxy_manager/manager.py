#!/usr/bin/env python
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

import os
import re
import glob

from haproxy_manager.config_files import ConfigFiles


class Manager(object):

    def __init__(self, main_path="/etc/haproxy/conf.d/"):
        self.main_path = main_path
        self.config_files = ConfigFiles(self.main_path)

    def list(self, ftype):
        # Get the file name
        # 90-frontend-machine0001.cfg
        #             ^^^^^^^^^^^
        regex = r'.*-([a-zA-Z0-9]+).cfg'

        files = [
            {"name": re.match(regex, f).group(1)}
            for f in glob.glob(self.main_path + "/*%s-*.cfg" % ftype)
            if os.path.isfile(f)
        ]
        return files

    def get(self, ftype, fname):
        try:
            return self.config_files.read(ftype, fname)
        except IOError:
            return {}

    def update(self, ftype, fname, opts):
        self.config_files.update(ftype, fname, opts)

    def delete(self, ftype, fname):
        self.config_files.remove(ftype, fname)
