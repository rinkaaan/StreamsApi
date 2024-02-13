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

yt-dlp "https://stream01.willfonk.com/live_playlist.m3u8?cid=BS296&r=FHD&ccode=JP&m=d0:20:20:04:35:cc&t=0d6938cb3dcf4b79848bc1753a59daf1"

yt-dlp "https://hls083.vipdracdn.net/streamhls2024/f89a76c7067505e25320415e0072de59/ep.2.v0.1707367415.720.m3u8"
auto_subtitle improper2.mp4 -o improper2_en --language ja --output_srt

yt-dlp "https://hls084.vipdracdn.net/streamhls2024/f89a76c7067505e25320415e0072de59/ep.3.v0.1707641216.720.m3u8" -o ep3.mp4
auto_subtitle ep3.mp4 -o ep3_.srt --language ja --output_srt true --output_dir . --srt_only true
