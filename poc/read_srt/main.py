import json


def time_to_seconds(time_str):
    """
    Convert a time string in the format 'HH:MM:SS,MS' to seconds.
    """
    hours, minutes, seconds_milliseconds = time_str.split(':')
    seconds, milliseconds = seconds_milliseconds.split(',')
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000
    return total_seconds


def parse_srt(srt_file_path):
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        blocks = file.read().strip().split('\n\n')

    subtitles = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            subtitle_number = int(lines[0])
            time_range = lines[1]
            start_time_str, end_time_str = time_range.split(' --> ')
            start_time = time_to_seconds(start_time_str)
            end_time = time_to_seconds(end_time_str)
            subtitle_text = '\n'.join(lines[2:])
            subtitles.append({
                # 'number': subtitle_number,
                'start': start_time,
                'end': end_time,
                'text': subtitle_text
            })

    return subtitles


# Example usage
srt_file_path = 'tbs mar 05 14 59 58.srt'
subtitles = parse_srt(srt_file_path)
# for subtitle in subtitles:
#     print(subtitle)

with open('tbs mar 05 14 59 58.json', 'w', encoding='utf-8') as file:
    json.dump(subtitles, file, ensure_ascii=False, indent=4)
