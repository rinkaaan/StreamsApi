import os
import signal
import subprocess
from datetime import datetime
import time

import pytz

japan_timezone = pytz.timezone('Asia/Tokyo')
japan_time = datetime.now(japan_timezone)
output_filename = f'{japan_time.strftime("%A").lower()} {time.strftime("%H-%M")}'
stream_url = 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1'
command = f'ffmpeg -i "{stream_url}" -c copy -bsf:a aac_adtstoasc "{output_filename}.mp4"'
print(command)

recording_process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(f"Recording started with PID {recording_process.pid}")
print(f"Recording started for {output_filename}")
print(f"Return code: {recording_process.returncode}")

time.sleep(3)

os.killpg(os.getpgid(recording_process.pid), signal.SIGINT)
