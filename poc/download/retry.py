import subprocess
import time
from datetime import datetime

import pytz

# Base FFmpeg command without the output file specified
# 1 hour = 3600 seconds
# base_ffmpeg_command = ['ffmpeg', '-i', 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1', '-t', '3600', '-c', 'copy']

base_ffmpeg_command = ['ffmpeg', '-i', 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1', '-t', '3600', '-c', 'copy']


def get_japan_time():
    japan_timezone = pytz.timezone('Asia/Tokyo')
    japan_time = datetime.now(japan_timezone)
    formatted = japan_time.strftime("%b %d %H %M %S").lower()
    return formatted


def run_ffmpeg(command):
    try:
        # Run the FFmpeg command
        subprocess.run(command, check=False)  # We ignore the exit code here
        print("FFmpeg process finished. Preparing to restart...")
    except Exception as e:
        print(f"FFmpeg process encountered an error: {e}. Attempting to restart...")


# Loop to continuously run FFmpeg with a new output file each time it exits
while True:
    # Generate the output file nam
    output_file = f"tbs {get_japan_time()}.mp4"
    print(f'Recording "{output_file}"')

    # Update the FFmpeg command with the new output file
    ffmpeg_command = base_ffmpeg_command + [output_file]

    # Run FFmpeg
    run_ffmpeg(ffmpeg_command)

    # Optional: Add a short delay  before restarting to prevent hammering in case of immediate failures
    time.sleep(1)
