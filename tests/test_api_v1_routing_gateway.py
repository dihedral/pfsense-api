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

class APIE2ETestRoutingGateway(e2e_test_framework.APIE2ETest):
    uri = "/api/v1/routing/gateway"
    get_tests = [{"name": "Read all routing gateways"}]
    post_tests = [
        {
            "name": "Create routing gateway",
            "payload": {
                "interface": "wan",
                "name": "API_e2e_test_GATEWAY",
                "ipprotocol": "inet",
                "gateway": "172.16.209.1",
                "monitor": "172.16.209.250",
                "descr": "E2E test"
            }
        },
        {
            "name": "Check interface requirement",
            "status": 400,
            "return": 6007
        },
        {
            "name": "Check interface exists constraint",
            "status": 400,
            "return": 6008,
            "payload": {
                "interface": "INVALID"
            }
        },
        {
            "name": "Check IP protocol requirement",
            "status": 400,
            "return": 6009,
            "payload": {
                "interface": "wan"
            }
        },
        {
            "name": "Check IP protocol choice constraint",
            "status": 400,
            "return": 6010,
            "payload": {
                "interface": "wan",
                "ipprotocol": "INVALID"
            }
        },
        {
            "name": "Check name requirement",
            "status": 400,
            "return": 6011,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet"
            }
        },
        {
            "name": "Check name character constraint",
            "status": 400,
            "return": 6012,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "!@#INVALID NAME<>?^&*()"
            }
        },
        {
            "name": "Check name unique constraint",
            "status": 400,
            "return": 6026,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "WAN_DHCP"
            }
        },
        {
            "name": "Check gateway address requirement",
            "status": 400,
            "return": 6013,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST"
            }
        },
        {
            "name": "Check gateway address validation",
            "status": 400,
            "return": 6014,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST",
                "gateway": "INVALID GATEWAY ADDRESS"
            }
        },
        {
            "name": "Check non-dynamic interface gateway constraint",
            "status": 400,
            "return": 6029,
            "payload": {
                "interface": "lan",
                "ipprotocol": "inet",
                "name": "TEST",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check dynamic IPv4 gateway override",
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "DYNAMICv4",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check dynamic IPv4 gateway override maximum constraint",
            "status": 400,
            "return": 6029,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "NEWDYNAMICv4",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check dynamic IPv6 gateway override",
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "DYNAMICv6",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check dynamic IPv6 gateway override maximum constraint",
            "status": 400,
            "return": 6029,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "NEWDYNAMICv6",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check monitor IP validation",
            "status": 400,
            "return": 6025,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "monitor": "0::"
            }
        },
        {
            "name": "Check weight minimum constraint",
            "status": 400,
            "return": 6015,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "weight": 0
            }
        },
        {
            "name": "Check weight maximum constraint",
            "status": 400,
            "return": 6015,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "weight": 31
            }
        },
        {
            "name": "Check data payload minimum constraint",
            "status": 400,
            "return": 6016,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "data_payload": 0
            }
        },
        {
            "name": "Check low latency minimum constraint",
            "status": 400,
            "return": 6017,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "latencylow": 0
            }
        },
        {
            "name": "Check high latency minimum constraint",
            "status": 400,
            "return": 6018,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "latencylow": 5,
                "latencyhigh": 4
            }
        },
        {
            "name": "Check low loss minimum constraint",
            "status": 400,
            "return": 6019,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "losslow": 0
            }
        },
        {
            "name": "Check low loss maximum constraint",
            "status": 400,
            "return": 6019,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "losslow": 101
            }
        },
        {
            "name": "Check high loss minimum constraint",
            "status": 400,
            "return": 6020,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "losslow": 99,
                "losshigh": 50
            }
        },
        {
            "name": "Check high loss minimum constraint",
            "status": 400,
            "return": 6020,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "losslow": 50,
                "losshigh": 101
            }
        },
        {
            "name": "Check interval minimum constraint",
            "status": 400,
            "return": 6021,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "interval": 0
            }
        },
        {
            "name": "Check interval maximum constraint",
            "status": 400,
            "return": 6021,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "interval": 100000000000
            }
        },
        {
            "name": "Check loss interval minimum constraint",
            "status": 400,
            "return": 6022,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "loss_interval": 0
            }
        },
        {
            "name": "Check time period minimum constraint",
            "status": 400,
            "return": 6023,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "time_period": 0
            }
        },
        {
            "name": "Check alert interval minimum constraint",
            "status": 400,
            "return": 6024,
            "payload": {
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "TEST_MONITOR",
                "gateway": "172.16.77.200",
                "alert_interval": 0
            }
        }
    ]
    put_tests = [
        {
            "name": "Update routing gateway",
            "payload": {
                "id": 0,
                "name": "UPDATED_e2e_test_GATEWAY",
                "ipprotocol": "inet6",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "monitor": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "descr": "Updated E2E Test",
                "disabled": True,
                "action_disable": True,
                "monitor_disable": True,
                "weight": 2,
                "data_payload": 5,
                "latencylow": 300,
                "latencyhigh": 600,
                "interval": 2100,
                "loss_interval": 2500,
                "action_interval": 1040,
                "time_period": 66000,
                "losslow": 5,
                "losshigh": 10
            }
        },
        {
            "name": "Check ID requirement",
            "status": 400,
            "return": 6027
        },
        {
            "name": "Check ID exists constraint",
            "status": 400,
            "return": 6028,
            "payload": {
                "id": "INVALID"
            }
        },
        {
            "name": "Check interface exists constraint",
            "status": 400,
            "return": 6008,
            "payload": {
                "id": 0,
                "interface": "INVALID"
            }
        },
        {
            "name": "Check IP protocol choice constraint",
            "status": 400,
            "return": 6010,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "INVALID"
            }
        },
        {
            "name": "Check name character constraint",
            "status": 400,
            "return": 6012,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "!@#INVALID NAME<>?^&*()"
            }
        },
        {
            "name": "Check name unique constraint",
            "status": 400,
            "return": 6026,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "DYNAMICv6"
            }
        },
        {
            "name": "Check gateway address validation",
            "status": 400,
            "return": 6014,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST",
                "gateway": "INVALID GATEWAY ADDRESS"
            }
        },
        {
            "name": "Check non-dynamic interface gateway constraint",
            "status": 400,
            "return": 6029,
            "payload": {
                "id": 0,
                "interface": "lan",
                "ipprotocol": "inet",
                "name": "TEST",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check dynamic IPv4 gateway override maximum constraint",
            "status": 400,
            "return": 6029,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet",
                "name": "NEWDYNAMICv4",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check dynamic IPv6 gateway override maximum constraint",
            "status": 400,
            "return": 6029,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "NEWDYNAMICv6",
                "gateway": "dynamic"
            }
        },
        {
            "name": "Check monitor IP validation",
            "status": 400,
            "return": 6025,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "monitor": "172.16.77.50"
            }
        },
        {
            "name": "Check weight minimum constraint",
            "status": 400,
            "return": 6015,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "weight": 0
            }
        },
        {
            "name": "Check weight maximum constraint",
            "status": 400,
            "return": 6015,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "weight": 31
            }
        },
        {
            "name": "Check data payload minimum constraint",
            "status": 400,
            "return": 6016,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "data_payload": 0
            }
        },
        {
            "name": "Check low latency minimum constraint",
            "status": 400,
            "return": 6017,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "latencylow": 0
            }
        },
        {
            "name": "Check high latency minimum constraint",
            "status": 400,
            "return": 6018,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "latencylow": 5,
                "latencyhigh": 4
            }
        },
        {
            "name": "Check low loss minimum constraint",
            "status": 400,
            "return": 6019,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "losslow": 0
            }
        },
        {
            "name": "Check low loss maximum constraint",
            "status": 400,
            "return": 6019,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "losslow": 101
            }
        },
        {
            "name": "Check high loss minimum constraint",
            "status": 400,
            "return": 6020,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "losslow": 99,
                "losshigh": 50
            }
        },
        {
            "name": "Check high loss minimum constraint",
            "status": 400,
            "return": 6020,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "losslow": 50,
                "losshigh": 101
            }
        },
        {
            "name": "Check interval minimum constraint",
            "status": 400,
            "return": 6021,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "interval": 0
            }
        },
        {
            "name": "Check interval maximum constraint",
            "status": 400,
            "return": 6021,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "interval": 100000000000
            }
        },
        {
            "name": "Check loss interval minimum constraint",
            "status": 400,
            "return": 6022,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "loss_interval": 0
            }
        },
        {
            "name": "Check time period minimum constraint",
            "status": 400,
            "return": 6023,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "time_period": 0
            }
        },
        {
            "name": "Check alert interval minimum constraint",
            "status": 400,
            "return": 6024,
            "payload": {
                "id": 0,
                "interface": "wan",
                "ipprotocol": "inet6",
                "name": "TEST_MONITOR",
                "gateway": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "alert_interval": 0
            }
        }
    ]
    delete_tests = [
        {
            "name": "Check ID requirement",
            "status": 400,
            "return": 6027
        },
        {
            "name": "Check ID exists constraint",
            "status": 400,
            "return": 6028,
            "payload": {
                "id": "INVALID"
            }
        },
        {
            "name": "Delete routing gateway",
            "payload": {
                "id": 0
            },
            "resp_time": 5    # Allow a few seconds to safely remove the gateway and reload the route table
        },
        {
            "name": "Delete dynamic IPv4 gateway override",
            "payload": {
                "id": 0
            },
            "resp_time": 5    # Allow a few seconds to safely remove the gateway and reload the route table
        },
        {
            "name": "Delete dynamic IPv6 gateway override",
            "payload": {
                "id": 0,
                "apply": True
            },
            "resp_time": 5    # Allow a few seconds to safely remove the gateway and reload the route table
        }
    ]

APIE2ETestRoutingGateway()
