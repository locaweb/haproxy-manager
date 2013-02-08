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

from haproxy_manager.file_writers.writer import Writer

from Cheetah.Template import Template


class Global(Writer):

    def __init__(self):
        super(Global, self).__init__()
        self.output_path = '/etc/haproxy/conf.d/00-global.conf'

    def write_file(self):
        self.write('global', self.output_path, {'maxconn': 10000})
