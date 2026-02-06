ffmpeg -re -stream_loop -1 -i ./video/{VIDEO} \
-r 30 -pix_fmt yuv420p \
-c:v libx264 -profile:v high -level 4.0 -g 60 -keyint_min 60 \
-preset veryfast -b:v 2500k -maxrate 2500k -bufsize 5000k \
-c:a aac -b:a 128k -ar 44100 \
-flvflags no_duration_filesize \
-f flv "rtmps://va.pscp.tv:443/x/{TOKEN}"
