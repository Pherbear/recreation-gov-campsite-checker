# python camping.py --start-date 2025-08-28 --end-date 2025-09-01 --stdin < parks.txt | python notifier.py
# to run command every 3 minutes in cron

import subprocess
import time

start_date = '2025-08-28'
end_date = '2025-09-01'
park_ids = 'parks.txt'
time_ms = 180

def run_scripts():
    command = f'python camping.py --start-date {start_date} --end-date {end_date} --stdin < {park_ids} | python notifier.py'
    subprocess.run(command, shell=True)

while True:
    run_scripts()
    print('waiting 3 minutes')
    time.sleep(time_ms)  # 180 seconds = 3 minutes