#!/usr/bin/python3

import os
from pathlib import Path
import subprocess

### GLOBAL VARIABLES ###
script_name = os.path.basename(__file__)
script_path = Path(os.path.abspath(__file__))
script_dir = script_path.parents[0]
read_one_script = os.path.join(script_dir, "read_one.py")
devices = [
    "dlink-cam",
    "philips-hue",
    "tplink-plug",
    "xiaomi-cam"
]

# Program entry point
if __name__ == "__main__":

    for device in devices:
        # Read the list of timestamps
        device_path = os.path.join(script_dir, device)
        for scenario in [os.path.basename(f.path) for f in os.scandir(device_path) if f.is_dir() and len(os.listdir(f.path)) > 0]:
            cmd = f"python3 {read_one_script} {device} {scenario}"
            subprocess.run(cmd.split())
