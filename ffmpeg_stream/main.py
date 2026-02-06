import argparse
import signal
import subprocess
import sys
import time
from pathlib import Path

DEFAULT_URL_TEMPLATE = "rtmps://va.pscp.tv:443/x/{TOKEN}"
RESTART_BACKOFF_SEC = 3

proc: subprocess.Popen | None = None


def build_url(url_template: str, token: str) -> str:
    """Build the final URL from the template and token."""
    if "{TOKEN}" in url_template:
        return url_template.replace("{TOKEN}", token)
    if url_template.endswith("/"):
        return url_template + token
    if url_template.split("/")[-1] == "x":
        return url_template + "/" + token
    return url_template


def build_ffmpeg_cmd(video_path: Path, publish_url: str) -> list[str]:
    """Construct the ffmpeg command according to the given template."""
    return [
        "ffmpeg",
        "-re",
        "-stream_loop",
        "-1",
        "-i",
        str(video_path),
        "-r",
        "30",
        "-pix_fmt",
        "yuv420p",
        "-c:v",
        "libx264",
        "-profile:v",
        "high",
        "-level",
        "4.0",
        "-g",
        "60",
        "-keyint_min",
        "60",
        "-preset",
        "veryfast",
        "-b:v",
        "2500k",
        "-maxrate",
        "2500k",
        "-bufsize",
        "5000k",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-ar",
        "44100",
        "-flvflags",
        "no_duration_filesize",
        "-f",
        "flv",
        publish_url,
    ]


def start_ffmpeg(cmd: list[str]) -> subprocess.Popen:
    print("🚀 Starting ffmpeg:\n ", " ".join(cmd))
    return subprocess.Popen(cmd)


def stop_ffmpeg(p: subprocess.Popen | None):
    if p and p.poll() is None:
        print("🛑 Stopping ffmpeg...")
        p.terminate()
        try:
            p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            p.kill()


def signal_handler(sig, frame):
    global proc  # noqa
    stop_ffmpeg(proc)
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Simple ffmpeg streamer wrapper")
    parser.add_argument("--video", required=True, help="Path to video file")
    parser.add_argument("--token", required=True, help="Stream key/token")
    parser.add_argument(
        "--url",
        default=DEFAULT_URL_TEMPLATE,
        help="RTMP(S) URL template (default: %(default)s)",
    )
    args = parser.parse_args()

    video_path = Path(args.video)
    if not video_path.exists():
        print(f"❌ Video file not found: {video_path}")
        sys.exit(1)

    publish_url = build_url(args.url, args.token)
    cmd = build_ffmpeg_cmd(video_path, publish_url)

    global proc
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        proc = start_ffmpeg(cmd)
        ret = proc.wait()
        if ret == 0:
            print("✅ ffmpeg exited cleanly.")
            break
        else:
            print(
                f"⚠️ ffmpeg crashed with code {ret}, restarting in {RESTART_BACKOFF_SEC} sec..."
            )
            time.sleep(RESTART_BACKOFF_SEC)


if __name__ == "__main__":
    main()
