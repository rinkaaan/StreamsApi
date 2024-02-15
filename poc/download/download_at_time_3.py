import os
import signal
import subprocess
import time
from datetime import datetime, timedelta

import pytz

weekly_schedule = {
    'Monday': [],
    'Tuesday': [
        # eye love you
        ('22:00', '22:57', 'eye love you'),
        # test
        ('14:55', '14:56', 'test')
    ],
    'Wednesday': [
        # breaking the melon
        ('0:58', '1:28', 'breaking the melon')
    ],
    'Thursday': [],
    'Friday': [
        # inappropriateness
        ('22:00', '22:54', 'inappropriateness')
    ],
}


def start_recording(output_filename):
    stream_url = 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1'
    global recording_process
    # command = f'yt-dlp -o "{output_filename}.%(ext)s" "{stream_url}"'

    # ffmpeg -i "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" -c copy -bsf:a aac_adtstoasc output.mp4
    command = f'ffmpeg -i "{stream_url}" -c copy -bsf:a aac_adtstoasc "{output_filename}.mp4"'

    # Start the yt-dlp command in a subprocess; also store success code
    recording_process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
    # print(f"Recording started with PID {recording_process.pid}")
    print(f"Recording started for {output_filename}")

    # print("start_recording called")


def stop_recording():
    global recording_process
    if recording_process:
        # Send SIGINT to the process group to gracefully stop yt-dlp
        os.killpg(os.getpgid(recording_process.pid), signal.SIGINT)
        print("SIGINT signal sent to stop recording.")
    else:
        print("No recording process found.")

    # print("stop_recording called")


def do_this():
    # Set the timezone to Japan
    japan_timezone = pytz.timezone('Asia/Tokyo')

    # Get the current time in Japan
    japan_time = datetime.now(japan_timezone)

    # Print the day of the week
    # print("Day of the Week in Japan:", japan_time.strftime('%A'))

    # Print the current time in Japan in 24-hour format
    print("Current Time in Japan (24-hour format):", japan_time.strftime('%H:%M:%S'))

    # Print the current time in Japan in AM/PM format
    # print("Current Time in Japan (AM/PM format):", japan_time.strftime('%I:%M:%S %p'))

    current_time = japan_time.strftime('%H:%M:%S')

    if japan_time.strftime('%A') in weekly_schedule:
        for start_time, end_time, show in weekly_schedule[japan_time.strftime('%A')]:

            # decrement start_time by 2 minutes
            start_time = datetime.strptime(start_time, '%H:%M')
            # start_time = start_time - timedelta(minutes=2)
            start_time = start_time.strftime('%H:%M') + ':00'

            # increment end_time by 2 minutes
            end_time = datetime.strptime(end_time, '%H:%M')
            # end_time = end_time + timedelta(minutes=2)
            end_time = end_time.strftime('%H:%M') + ':00'

            # print(f"start_time: {start_time}, end_time: {end_time}, current_time: {current_time}, day: {japan_time.strftime('%A')}")

            # get current japan time in 24-hour format and day
            # e.g. tbs eye love you Feb 22
            output_filename = f'tbs {show} {japan_time.strftime("%b %d")}'

            if current_time == start_time:
                start_recording(output_filename)
            if current_time == end_time:
                stop_recording()


def print_time_every_second():
    next_time = time.time() + 1
    while True:
        now = time.time()
        if now >= next_time:
            # Update the next_time by adding 1 second
            next_time += 1

            # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))
            do_this()

            # Calculate the delay to adjust for the execution time of the loop
            delay = next_time - time.time()
            if delay > 0:
                time.sleep(delay)


print_time_every_second()
