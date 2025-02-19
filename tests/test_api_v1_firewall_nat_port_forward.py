# Copyright 2022 Jared Hendrickson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import e2e_test_framework

class APIE2ETestFirewallNATPortForward(e2e_test_framework.APIE2ETest):
    uri = "/api/v1/firewall/nat/port_forward"
    get_tests = [
        {"name": "Read all NAT port forwards"}
    ]
    post_tests = [
        {
            "name": "Create NAT port forward",
            "payload": {
                "interface": "WAN",
                "protocol": "tcp",
                "src": "any",
                "srcport": "433",
                "dst": "wanip",
                "dstport": "443",
                "target": "192.168.1.123",
                "local-port": "443",
                "natreflection": "purenat",
                "descr": "E2E Test",
                "nosync": True,
                "top": True
            }
        }
    ]
    put_tests = [
        {
            "name": "Update NAT port forward and apply",
            "payload": {
                "id": 0,
                "interface": "WAN",
                "protocol": "tcp",
                "src": "!1.1.1.1/24",
                "srcport": "any",
                "dst": "wanip",
                "dstport": 80,
                "target": "192.168.1.1",
                "local-port": "80",
                "natreflection": "enable",
                "descr": "Updated E2E Test",
                "nosync": False,
                "nordr": True,
                "disabled": True,
                "top": True,
                "apply": True
            },
            "resp_time": 3    # Allow a few seconds for the firewall filter to reload
        }
    ]
    delete_tests = [
        {"name": "Delete NAT port forward", "payload": {"id": 0}}
    ]

APIE2ETestFirewallNATPortForward()
