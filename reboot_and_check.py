import pandas as pd
import subprocess
import time
import os
import logging
from tqdm import tqdm

# Set up logging
logging.basicConfig(filename='failed_to_up.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Read the Excel file
df = pd.read_excel('unreachable.xlsx')

# Get the list of IP addresses and device IDs
ip_addresses = df.iloc[:, 0]
device_ids = df.iloc[:, 4]

# Reboot devices
for device_id in tqdm(device_ids, desc='Rebooting devices'):
    try:
        subprocess.run(['metal', 'device', 'reboot', '-i', device_id], check=True)
    except subprocess.CalledProcessError as e:
        logging.info(f'Failed to reboot device with ID {device_id}: {e}')

# Wait for 10 minutes to allow servers to come online
time.sleep(600)

# Check if servers are reachable
for ip in tqdm(ip_addresses, desc='Pinging servers'):
    response = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
    if response.returncode != 0:
        logging.info(f'Server with IP {ip} is not reachable after 10 minutes.')

print("Script completed. Check 'failed_to_up.log' for details of servers that were not reachable.")

