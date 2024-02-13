import subprocess
import schedule
import time
import os
import signal


def start_recording():
    # get current japan time in 24-hour format and day of week
    # e.g. tuesday 22-00
    output_filename = f'{time.strftime("%A").lower()} {time.strftime("%H-%M")}.%(ext)s'

    # global recording_process
    # command = f'yt-dlp -o "{output_filename}" "{stream_url}"'
    # # Start the yt-dlp command in a subprocess
    # recording_process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
    # print(f"Recording started with PID {recording_process.pid}")
    print("start_recording called")


def stop_recording():
    # global recording_process
    # if recording_process:
    #     # Send SIGINT to the process group to gracefully stop yt-dlp
    #     os.killpg(os.getpgid(recording_process.pid), signal.SIGINT)
    #     print("SIGINT signal sent to stop recording.")
    # else:
    #     print("No recording process found.")
    print("stop_recording called")


# Example schedule for multiple start and end times for each day
weekly_schedule = {
    'Monday': [],
    'Tuesday': [
        # eye love you
        ('22:00', '22:57'),
    ],
    'Wednesday': [
        # breaking the melon
        ('0:58', '1:28')
    ],
    'Thursday': [],
    'Friday': [
        # inappropriateness
        ('22:00', '22:54')
    ],
}

stream_url = 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1'

# Eye Love You
schedule.every().tuesday.at('22:00:00', 'Japan').do(start_recording, stream_url=stream_url)
schedule.every().tuesday.at('22:57:00', 'Japan').do(stop_recording)

# Breaking the Melon
schedule.every().wednesday.at('00:58:00', 'Japan').do(start_recording, stream_url=stream_url)
schedule.every().wednesday.at('01:28:00', 'Japan').do(stop_recording)

# Inappropriateness
schedule.every().friday.at('22:00:00', 'Japan').do(start_recording, stream_url=stream_url)
schedule.every().friday.at('22:54:00', 'Japan').do(stop_recording)

# Test
schedule.every().tuesday.at('11:41:00', 'Japan').do(start_recording, stream_url=stream_url)
schedule.every().tuesday.at('11:42:00', 'Japan').do(stop_recording)

# Keep the script running to maintain the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
