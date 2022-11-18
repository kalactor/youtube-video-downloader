# Youtube Video Downloader

This python script uses Pytube library for downloading videos. One can use pytube directly in terminal to download videos but pytube only download upto 720p directly. Downloading 1080p (Full HD) takes a little effort which repititive also that's why i made this script which download both video and audio stream from youtube using Pytube then merge them using FFMPEG.

<h2>Requirements</h2>
1. <a href="https://www.python.org/">Python</a> And <a href="https://pytube.io/en/latest/">Pytube</a> pyhton library </br>
2. <a href="https://ffmpeg.org/">FFMPEG</a> for merging 1080p video and audio stream </br>

<h2>Installation</h2>
<b>For Debian Distro</b> </br>
1. Python - <code> sudo apt install python3</code> </br>
2. Pytube - <code> pip install pytube</code> </br>
3. FFMPEG -  <code>sudo apt install ffmpeg</code> </br>
</br>
After installing requirements clone the repo <code>https://github.com/kalactor/youtube-video-downloader.git</code> </br>
Navigate to downloaded folder and hit <code> python3 youtube.py</code> or <code> python youtube.py</code> 

