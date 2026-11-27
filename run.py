#!/usr/bin/env -S python

from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from tinytag import TinyTag
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

def stop_video(pid):
    os.kill(pid, signal.SIGTERM)

def play_next_video():
    video_paths = get_video_paths()
    cur_video_id = os.getenv("LAST_VIDEO_PLAYED_ID")
    next_video_id = 0

    if cur_video_id < len(video_paths):
        next_video_id = cur_video_id + 1

    video_path = f"file:///{video_paths[next_video_id]}"
    stop_video(playing_video_pid)
    playing_video_pid = play_video(video_path)

# there needs to be more logic here, need the length of the videos
while True:
    cur_hour = datetime.now().hour

    if cur_hour <= end_hour:
        play_next_video()
    else:
        if playing_video_pid is not None:
            stop_video(playing_video_pid)
