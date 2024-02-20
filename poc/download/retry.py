import subprocess
import time

# Base FFmpeg command without the output file specified
# 1 hour = 3600 seconds
base_ffmpeg_command = ['ffmpeg', '-i', 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1', '-t', '3600', '-c', 'copy']

# Initial output file counter
file_counter = 1


# Function to generate output file name based on counter
def generate_output_filename(counter):
    return f"output_{counter}.mp4"


# Function to run FFmpeg
def run_ffmpeg(command):
    try:
        # Run the FFmpeg command
        subprocess.run(command, check=False)  # We ignore the exit code here
        print("FFmpeg process finished. Preparing to restart...")
    except Exception as e:
        print(f"FFmpeg process encountered an error: {e}. Attempting to restart...")


# Loop to continuously run FFmpeg with a new output file each time it exits
while True:
    # Generate the output file name
    output_file = generate_output_filename(file_counter)

    # Update the FFmpeg command with the new output file
    ffmpeg_command = base_ffmpeg_command + [output_file]

    # Run FFmpeg
    run_ffmpeg(ffmpeg_command)

    # Increment the counter for the next output file
    file_counter += 1

    # Optional: Add a short delay before restarting to prevent hammering in case of immediate failures
    time.sleep(1)
