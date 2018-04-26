#!/usr/bin/env python
"""
Connect to set of network devices using NAPALM (different platforms); print
out the facts.
"""
from __future__ import print_function, unicode_literals
from pprint import pprint
from napalm import get_network_driver
from my_devices import pynet_sw2

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    """
    Connect to set of network devices using NAPALM (different platforms); print
    out the facts.
    """
    for a_device in (pynet_sw2,):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        print()
        print(">>>Device open")
        device.open()

        print("-" * 50)
        bgp_info = device.get_interfaces()
        hostname = a_device['hostname']
        print("{hostname}:\n".format(hostname=hostname))
        pprint(bgp_info)
        print()

    print()


if __name__ == "__main__":
    main()
