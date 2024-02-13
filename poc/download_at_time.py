import datetime
import os
import signal
import subprocess
import schedule
import time


def start_recording(stream_url, output_filename):
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


# Define your .m3u8 stream URL and output filename here
stream_url = 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1'
output_filename = 'output_file.%(ext)s'

# Define start and end times here (24-hour format)
start_time = '11:59'
end_time = '12:00'

# Schedule the recording to start and stop at the defined times
schedule.every().tuesday.at(start_time, 'Japan').do(start_recording, stream_url=stream_url, output_filename=output_filename).until(datetime.timedelta(seconds=10))
schedule.every().tuesday.at(end_time, 'Japan').do(stop_recording).until(datetime.timedelta(seconds=10))


# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

# import subprocess
#
# subprocess.run('yt-dlp -o "output_file.mp4" "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1"', shell=True)
