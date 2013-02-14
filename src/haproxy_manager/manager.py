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

from haproxy_manager.config_files import ConfigFiles


class Manager(object):

    def __init__(self, main_path="/etc/haproxy/conf.d/"):
        self.main_path = main_path

    def list(self):
        # Get the file name
        # 90-frontend-machine0001.cfg
        #    ^^^^^^^^^^^^^^^^^^^^
        regex = r'^[^.][0-9]+-([a-zA-Z0-9-]*).cfg$'

        files = [
            {"name": re.match(regex, f).group(1)}
            for f in os.listdir(self.main_path)
            if re.match(regex, f) and os.path.isfile(self.main_path + f)
        ]
        return files

    def get(self, file_name):
        ftype, fname = file_name.split("-")
        try:
            c = ConfigFiles(self.main_path)
            return c.read(ftype, fname)
        except IOError:
            return {}

    def update(self):
        pass

    def delete(self):
        pass
