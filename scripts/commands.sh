curl 'https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1' \
  -H 'authority: stream01.willfonk.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9,ja;q=0.8' \
  -H 'origin: https://jpnews-video.com' \
  -H 'referer: https://jpnews-video.com/' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  --compressed

ffmpeg -i "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" -c copy -bsf:a aac_adtstoasc output.mp4

vlc "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" --sout "#transcode{vcodec=h264,acodec=aac}:std{access=file,mux=mp4,dst='video.mp4'}"
vlc "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" --sout=file/ps:go.mpg
vlc "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" --sout="#std{access=file,mux=ps,dst=go.mp4}"
vlc "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" --sout "#transcode{vcodec=h264,acodec=aac}:std{access=file,mux=mp4,dst='video.mp4'}"

quicktime
mp1v
mpga


ffmpeg -http_persistent 1 -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 60 -i "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" -c copy -bsf:a aac_adtstoasc "tbs feb 15.mp4"

ffmpeg -http_persistent 1 -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 60 -t 5 -i "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1" -c copy -bsf:a aac_adtstoasc "tbs.mp4"

yt-dlp "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1"

# This is the one!
yt-dlp --retries infinite --fragment-retries infinite --socket-timeout 9999 "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1"

yt-dlp "https://hls083.vipdracdn.net/streamhls2024/f89a76c7067505e25320415e0072de59/ep.2.v0.1707367415.720.m3u8"
auto_subtitle improper2.mp4 -o improper2_en --language ja --output_srt

yt-dlp "https://hls067.vipdracdn.net/streamhls2024/1d083add58333113de2545fa073818da/ep.8.v0.1680345949.480.m3u8" -o ep8.mp4
auto_subtitle ep8.mp4 -o ep8_.srt --language ja --output_srt true --output_dir . --srt_only true

#-rw-r--r-- 1 root root  289043635 Feb 13 17:15 'tbs breaking melon feb 14.mp4'
#-rw-r--r-- 1 root root  116655255 Feb 13 14:07 'tbs eyeloveyou feb 13.mp4'
#-rw-r--r-- 1 root root  969066186 Feb 13 15:56 'tbs news23 feb 13.mp4'
#-rw-r--r-- 1 root root  664351726 Feb 13 20:25 'tbs news feb 14.mp4'
#-rw-r--r-- 1 root root 2414412523 Feb 13 11:00 'tbs nstar feb 13.mp4'
#-rw-r--r-- 1 root root       4688 Feb 13 08:32  tbs.py
#-rw-r--r-- 1 root root  800157921 Feb 13 21:19 'tbs the time 1 feb 14.mp4'
#-rw-r--r-- 1 root root  428343344 Feb 13 21:45 'tbs the time 2 feb 14.mp4'

auto_subtitle 'tbs breaking melon feb 14.mp4' -o 'tbs breaking melon feb 14.srt' --language ja --output_srt true --output_dir . --srt_only true
auto_subtitle 'tbs eyeloveyou feb 13.mp4' -o 'tbs eyeloveyou feb 13.srt' --language ja --output_srt true --output_dir . --srt_only true
auto_subtitle 'tbs news23 feb 13.mp4' -o 'tbs news23 feb 13.srt' --language ja --output_srt true --output_dir . --srt_only true
auto_subtitle 'tbs news feb 14.mp4' -o 'tbs news feb 14.srt' --language ja --output_srt true --output_dir . --srt_only true
auto_subtitle 'tbs nstar feb 13.mp4' -o 'tbs nstar feb 13.srt' --language ja --output_srt true --output_dir . --srt_only true
auto_subtitle 'tbs the time 1 feb 14.mp4' -o 'tbs the time 1 feb 14.srt' --language ja --output_srt true --output_dir . --srt_only true
auto_subtitle 'tbs the time 2 feb 14.mp4' -o 'tbs the time 2 feb 14.srt' --language ja --output_srt true --output_dir . --srt_only true
