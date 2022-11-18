#!/bin/bash
echo Merging audio and video files
pwd
ffmpeg -i video.mp4 -i audio.webm -c:v copy -c:a copy output.mp4
