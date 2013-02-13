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


class ConfigWriter(object):

    def __init__(self, main_path="/etc/haproxy/"):
        self.main_path = main_path
        self.config_file = ""

    def concat(self):
        path = self.main_path + "conf.d/"
        files = [
            open(path + i).read()
            for i in os.listdir(path)
            if not re.match(r'\..*', i)  # Avoiding ".files"
        ]
        return "\n".join(files)

    def write(self, content):
        with open(self.main_path + "haproxy.cfg", 'w') as file:
            file.write(content)
