#!/bin/bash
echo merging audio and video
pwd
ffmpeg -i video.mp4 -i audio.webm -c:v copy -c:a copy output.mp4
