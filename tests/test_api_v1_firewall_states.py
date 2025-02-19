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

class APIE2ETestFirewallStates(e2e_test_framework.APIE2ETest):
    uri = "/api/v1/firewall/states"
    get_tests = [{"name": "Read all firewalls states"}]
    delete_tests = [
        {
            "name": "Check firewall state deletion",
            "payload": {"source": "1.2.3.4"}
        },
        {
            "name": "Check source requirement",
            "status": 400,
            "return": 4231
        },
        {
            "name": "Check source IP/CIDR constraint",
            "status": 400,
            "return": 4232,
            "payload": {"source": "INVALID"}
        },
        {
            "name": "Check destination IP/CIDR constraint",
            "status": 400,
            "return": 4233,
            "payload": {"source": "1.2.3.4", "destination": "INVALID"}
        },
        {
            "name": "Check sleep minimum constraint",
            "status": 400,
            "return": 4236,
            "payload": {"source": "1.2.3.4", "sleep": -1}
        },
        {
            "name": "Check sleep maximum constraint",
            "status": 400,
            "return": 4236,
            "payload": {"source": "1.2.3.4", "sleep": 301}
        }
    ]

APIE2ETestFirewallStates()
