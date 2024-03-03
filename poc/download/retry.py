import signal
import subprocess
import time
from datetime import datetime

import pytz

# Base FFmpeg command without the output file specified
# 1 hour = 3600 seconds
# base_ffmpeg_command = ['ffmpeg', '-i', 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1', '-t', '3600', '-c', 'copy']

# yt-dlp --retries infinite --fragment-retries infinite --socket-timeout 9999 "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" -o test.mp4
base_ffmpeg_command = [
    "yt-dlp",
    "--retries",
    "infinite",
    "--fragment-retries",
    "infinite",
    "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1",
    "-o",
]


def get_japan_time():
    japan_timezone = pytz.timezone('Asia/Tokyo')
    japan_time = datetime.now(japan_timezone)
    formatted = japan_time.strftime("%b %d %H %M %S").lower()
    return formatted


def run_ffmpeg(command):
    print("Starting ffmpeg...")
    # Start the yt-dlp process
    process = subprocess.Popen(command)

    try:
        process.wait(timeout=30 * 60)
        print("yt-dlp process finished within the timeout period.")
    except subprocess.TimeoutExpired:
        # If the process does not finish in 60 seconds, terminate it gracefully
        print("yt-dlp process did not finish in time. Attempting to terminate gracefully...")
        process.send_signal(signal.SIGINT)  # Send SIGINT to request graceful termination
        try:
            # Wait a bit for the process to terminate gracefully
            process.wait(timeout=5)
            print("yt-dlp process terminated gracefully.")
        except subprocess.TimeoutExpired:
            # If it still doesn't terminate, force termination
            print("Forcing yt-dlp process termination...")
            process.kill()
            process.wait()  # Ensure the process has been terminated
            print("yt-dlp process forcefully terminated.")
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
