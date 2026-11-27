#!/usr/bin/env -S python

from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import os
import signal
import subprocess

load_dotenv()
last_video_played_id = os.getenv("LAST_VIDEO_PLAYED_ID") # based on alpha sort array of videos in folder
start_hour = os.getenv("24_START_HOUR") or 9 # 9 AM
end_hour = os.getenv("24_END_HOUR") or 17 # 5 PM
env = os.environ.copy()
env["DISPLAY"] = ":0"
playing_video_pid = 0

def get_video_paths():
    folder = Path("./videos")
    paths = []

    for idx, file_path in enumerate(folder.glob(".mp4")):
        paths.append(file_path.name)

    return sorted(paths)

video_paths = get_video_paths()

video_path = f"file:///{video_paths[0]}"

def play_video(video_path):
    cmd = [
        "dbus-run-session",
        "--",
        "chromium",
        "--kiosk",
        "--user-data-dir=/tmp/chrome-kiosk",
        "--noerrdialogs",
        "--disable-infobars",
        "--log-level=3",
        "--autoplay-policy=no-user-gesture-required",
        "--no-sandbox",
        video_path
    ]

    process = subprocess.Popen(cmd, env=env)
    return process

def stop_video(process_pid):
    os.kill(process_pid, signal.SIGTERM)

# there needs to be more logic here, need the length of the videos
while True:
    cur_hour = datetime.now().hour

    if cur_hour <= end_hour:

    else:
