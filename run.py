#!/usr/bin/env -S python

import os
import subprocess

env = os.environ.copy()
env["DISPLAY"] = ":0"

video_paths = [
    "/home/pi/bird-videos/vid1.mp4",
    "/home/pi/bird-videos/vid2.mp4",
    "/home/pi/bird-videos/vid3.mp4",
    "/home/pi/bird-videos/vid4.mp4"
]

video_path = f"file:///{video_paths[0]}"

# Run a simple command
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

# Capture the output and check for errors
# result = subprocess.run(
    # ["echo", "Hello from CLI"], 
    # capture_output=True, 
    # text=True, 
    # check=True
# )

# print("Output:", result.stdout.strip())
# print("Return Code:", result.returncode)
