import os
import signal
import subprocess
import time
from datetime import datetime

import pytz

stream_url = 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1'
channel = 'tbs'

weekly_schedule = {
    'Monday': [
        ('04:00', '04:29', 'news'),
        ('04:30', '05:19', 'the time 1'),
        ('05:20', '08:00', 'the time 2'),
        ('10:25', '13:54', 'hiruobi'),
        ('13:55', '15:48', 'gogosuma'),
        ('15:49', '19:00', 'nstar'),
        ('22:57', '23:56', 'news23'),
    ],
    'Tuesday': [
        ('03:45', '04:29', 'news'),
        ('04:30', '05:19', 'the time 1'),
        ('05:20', '08:00', 'the time 2'),
        ('10:25', '13:54', 'hiruobi'),
        ('13:55', '15:49', 'gogosuma'),
        # ('15:49', '19:00', 'nstar'),
        ('16:33', '19:00', 'nstar'),
        ('22:00', '22:57', 'eyeloveyou'),
        ('22:57', '23:56', 'news23'),
    ],
    'Wednesday': [
        ('00:58', '01:28', 'breaking melon'),
        ('03:45', '04:29', 'news'),
        ('04:30', '05:19', 'the time 1'),
        ('05:20', '08:00', 'the time 2'),
        ('10:25', '13:54', 'hiruobi'),
        ('13:55', '15:49', 'gogosuma'),
        ('15:49', '19:00', 'nstar'),
        ('22:00', '22:57', 'eyeloveyou'),
        ('22:58', '23:56', 'news23'),
    ],
    'Thursday': [
        ('03:45', '04:29', 'news'),
        ('04:30', '05:19', 'the time 1'),
        ('05:20', '08:00', 'the time 2'),
        ('10:25', '13:54', 'hiruobi'),
        ('13:55', '15:49', 'gogosuma'),
        ('15:49', '19:00', 'nstar'),
        ('22:58', '23:56', 'news23'),
    ],
    'Friday': [
        ('01:28', '01:58', 'witch and beast'),
        ('03:45', '04:29', 'news'),
        ('04:30', '05:19', 'the time 1'),
        ('05:20', '08:00', 'the time 2'),
        ('10:25', '13:54', 'hiruobi'),
        ('13:55', '15:49', 'gogosuma'),
        ('15:49', '19:00', 'nstar'),
        ('22:00', '22:54', 'inappropriateness'),
        ('23:58', '_', 'news23'),
    ],
    'Saturday': [
        ('_', '00:48', 'news23'),
        ('04:00', '04:29', 'news'),
        ('17:30', '18:50', 'report special collection'),
        ('18:51', '21:00', 'job tune'),
        ('22:00', '23:30', 'information 7 days'),
    ],
    'Sunday': [
        ('05:00', '05:30', 'news'),
        ('08:00', '09:54', 'sunday morning'),
        ('09:54', '11:40', 'sunday japon'),
    ]
}


def start_recording():
    global recording_process
    global output_filename
    command = f'ffmpeg -i "{stream_url}" -c copy -bsf:a aac_adtstoasc "{output_filename}"'
    recording_process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
    print(f"Recording started for {output_filename}")


def stop_recording():
    global recording_process
    if recording_process:
        # Send SIGINT to the process group to gracefully stop yt-dlp
        os.killpg(os.getpgid(recording_process.pid), signal.SIGINT)
        print("SIGINT signal sent to stop recording.")

        time.sleep(5)

        command = f'auto_subtitle "{output_filename}" -o "{output_filename}.srt" --language ja --output_srt true --output_dir . --srt_only true'
        subprocess.run(command, shell=True)
        print(f"Subtitles generated for {output_filename}")
    else:
        print("No recording process found.")


def do_this():
    global output_filename
    # Set the timezone to Japan
    japan_timezone = pytz.timezone('Asia/Tokyo')

    # Get the current time in Japan
    japan_time = datetime.now(japan_timezone)
    current_time = japan_time.strftime('%H:%M:%S')

    if japan_time.strftime('%A') in weekly_schedule:
        for start_time, end_time, show in weekly_schedule[japan_time.strftime('%A')]:

            if start_time != '_':
                # decrement start_time by 2 minutes
                start_time = datetime.strptime(start_time, '%H:%M')
                # start_time = start_time - timedelta(minutes=2)
                start_time = start_time.strftime('%H:%M') + ':00'

            if end_time != '_':
                # increment end_time by 2 minutes
                end_time = datetime.strptime(end_time, '%H:%M')
                # end_time = end_time + timedelta(minutes=2)
                end_time = end_time.strftime('%H:%M') + ':00'

            output_filename = f'{channel} {show} {japan_time.strftime("%b %d").lower()}.mp4'

            if current_time == start_time:
                start_recording()
            if current_time == end_time:
                stop_recording()


def print_time_every_second():
    next_time = time.time() + 1
    while True:
        now = time.time()
        if now >= next_time:
            # Update the next_time by adding 1 second
            next_time += 1

            do_this()

            # Calculate the delay to adjust for the execution time of the loop
            delay = next_time - time.time()
            if delay > 0:
                time.sleep(delay)


print_time_every_second()
