#    Copyright 2013 Stephen Gran <sgran@debian.org>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
from six.moves import configparser

class Config(object):
    def __init__(self, options):

        if getattr(options, 'section', None) is None:
            raise AttributeError("need to know section")

        self.files = ['/etc/dsa/pubsub.conf',
                      os.path.expanduser('~/.pubsub.conf')]
        self.entries = ['username', 'password', 'vhost', 'exchange',
                        'topic', 'queue', 'git', 'debug']
        self.config = {}

        config = configparser.ConfigParser()

        if getattr(options, 'config', None):
            self.files.append(options.config)

        files = config.read(self.files)

        for entry in config.options(options.section):
            if entry in self.entries:
                self.config[entry] = config.get(options.section, entry)

        for entry in self.entries:
            if getattr(options, entry, None):
                self.config[entry] = getattr(options, entry)

    def __getattr__(self, key, default=None):
        return self.config.get(key, default)
