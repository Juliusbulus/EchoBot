# ffmpeg-stream

A lightweight alternative to OBS for streaming using FFmpeg.  
Runs without GUI and consumes fewer resources.

## Usage

```bash
python3 main.py --video ./video/1st.mov --token <STREAM_KEY>
```

Optional: specify custom RTMP(S) URL template:

```bash
python3 main.py --video ./video/clip.mov --token <STREAM_KEY> --url "rtmps://server/app/{TOKEN}"
```