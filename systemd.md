### Create a service

You can name the service whatever you want.

```
$sudo nano /etc/systemd/system/auto-vid-player.service
$sudo systemctl enable auto-vid-player.service
$sudo systemctl daemon-reload
$sudo systemctl restart auto-vid-player.service
```

#### auto-vid--player.service contents

```
[Unit]
Description=Start Auto Vid Player
After=multi-user.target

[Service]
Type=idle
WorkingDirectory=/home/pi/auto-vid-player
User=root
ExecStart=xinit ./openbox
Restart=always

[Install]
WantedBy=multi-user.target
```

Openbox will launch a window which will run run.py which launches and manages Chromium instances to play .mp4 videos based on length and a start/end play schedule
