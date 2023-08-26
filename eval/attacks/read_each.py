#!/usr/bin/python3

import os
from pathlib import Path
import subprocess

### GLOBAL VARIABLES ###
script_name = os.path.basename(__file__)
script_path = Path(os.path.abspath(__file__))
script_dir = script_path.parents[0]
read_one_script_name = "read_latency.py"
exp_cases = {
    "philips-hue_https-flood": [
        "no-attack",
        "with-attack"
    ],
    "tplink-plug_tcp-flood": [
        "no-attack",
        "with-attack"
    ],
    "tplink-plug_tcp-without-arp": [
        "no-attack",
        "with-attack"
    ],
    "tplink-plug_https-without-dns": [
        "no-attack",
        "with-attack"
    ]
}

# Program entry point
if __name__ == "__main__":

    for case, scenarios in exp_cases.items():
        device, attack = case.split("_")
        device_path = os.path.join(script_dir, device)
        case_path = os.path.join(device_path, attack)
        read_one_script = os.path.join(device_path, read_one_script_name)
        for scenario in scenarios:
            cmd = f"python3 {read_one_script} {attack} {scenario}"
            subprocess.run(cmd.split())
