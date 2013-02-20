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
import signal

from haproxy_manager.common.config import config


class Haproxy(object):

    def __init__(self, main_path="/etc/haproxy/"):
        self.main_path = main_path

    def concat_files(self):
        path = self.main_path + "conf.d/"
        files = [
            open(path + i).read()
            for i in os.listdir(path)
            if not re.match(r'\..*', i)  # Avoiding ".files"
        ]
        return "\n".join(files)

    def write_config(self, content):
        with open(self.main_path + "haproxy.cfg", 'w') as file:
            file.write(content)

    def restart(self):
        pid = config.get("haproxyfiles", "pid_file")

        try:
            with open(pid) as f:
                pids = f.read()
                print pids
                os.kill(pids, signal.SIGTTOU)
                os.kill(pids, signal.SIGTTIN)
        except:
            print "Missing pid file to restart gracefully. Cannot restart."
