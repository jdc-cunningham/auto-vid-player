- [x] basic functionality (load, play videos)
- [ ] scheduler
  - needs time of video (use ffmpeg)
  - use 24 hr to keep time range simple
  - start/end time range
  - main loop
  - chrome processes have an ID so they can be killed when time is up

### 11/26/2026

9:40 PM

Not really doing real work, I'm watching TV

These are the new ideas I had:

- start, end hours based on 24 hours (don't have to deal with AM/PM)
- a state that tracks last video so the video keeps cycling over the days
- not having to hardcode video file names

This is still not intended to be a very well polished thing but it would be nice when I'm lazy to just dump more videos into a folder, I guess that means the video list should refresh whenever it's looking for a new video to play

10:29 PM

Yeah this is already getting out of hand

The duration of each video can be determined calling ffmpeg but then that value should be stored somewhere

When is it computed?

You enumerate over a folder of videos... then when you need to use one you check how long it is, set an end date from when the video plays? What about the delay before it actually starts playing...

This doesn't have to be that accurate but yeah

It also doesn't matter if the video ends a second or two early

This dislay is small unfortunately hard to work in, reduce font size I guess

I'm working on this half-ass watching TV so not really thinking about it too much right now

10:33 PM

This library looks cool tinytag can tell how long a video is

10:53 PM

Alright I think this makes sense... using `os.environ` to write the playing video's details for determining if it should stop or not

If the script ends then the playing video doesn't matter anymore

The top-most control is the start/end hours

11:00 PM

Ugh... this is bad

There is also a problem where if the video stops playing since it ended... the loop has to catch that and start the next video

This could be simple just every second check if the video is still playing like PID check vs. tracking time

I need to check what happens when a video ends does the process end or is it still going but the video is just not playing anymore

In that case I would have to track the video duration against current time

---

### 11/24/2026

8:02 PM

I'm spent already today but I got the openbox chromium kiosk video player setup via systemd service
