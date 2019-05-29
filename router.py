import requests
import json
import re
import time
import csv

cookies = {
    'tomato_bw_24tab': 'br0',
    'tomato_bw_24refresh': '1',
    'tomato_status_devices_refresh': '3',
    'tomato_ipt_tab': '192.168.1.0',
    'tomato_ipt_graphs': '3',
    'tomato_ipt_addr_hidden': '192.168.1.33',
    'tomato_status_webmon_refresh': '3',
    'tomato_status_overview_refresh': '0',
    'tomato_ipt_details': '0',
    'tomato_bw_ravg': '1',
    'tomato_bw_rscale': '0',
    'tomato_bw_rdraw': '1',
    'tomato_bw_rtab': 'vlan2',
    'tomato_ipt_refresh': '0'
}

TIME_DELTA = 2

while True:
    speed = {}
    previous = {}

    while not speed:
        r = requests.post('http://192.168.1.1/update.cgi', data={'exec': 'netdev', '_http_id': 'TID6325354708c0cefa'},
                          auth=('admin', 'admin'))
        m = re.search(r'\'vlan2\':{rx:(\w+),tx:(\w+)}', r.text)
        rx_hex = m.group(1)
        tx_hex = m.group(2)
        rx = int(rx_hex, 0)
        tx = int(tx_hex, 0)
        if previous:
            speed['rx'] = round(
                (rx - int(previous['rx'])) / TIME_DELTA / 125000, 2)
            speed['tx'] = round(
                (tx - int(previous['tx'])) / TIME_DELTA / 125000, 2)
            break
        previous['rx'] = rx
        previous['tx'] = tx
        time.sleep(TIME_DELTA)

    print("RX: {} Mbit/s, TX: {} Mbit/s".format(speed['rx'], speed['tx']))
