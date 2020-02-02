If python3 is not currently installed download at: https://www.python.org/downloads/ (Not Necessary on linux, install via repositories.)
Be sure to check the tkinter option in the installer.
Once python3 has installed open your terminal: Windows win+r: cmd <Enter>
Once in the terminal, type the following: python -m pip install --upgrade pip # this updates pip to the latest version
When that completes type the following: pip install --upgrade youtube_dl # This installs the lates version of youtube-dl

Now that python and youtube_dl are installed, it is time to download ffmpeg. (not Necessary on linux since you can install via repositories.)
Go to: https://ffmpeg.org/download.html
Once you download your respective version of ffmpeg, extract it.
Note the location of the ffmpeg.exe file and paste it in the YoutubeDL.py file under the #Variables line in the quotes of the ffmpeg_location variable.
Save the YouTubeDL.py file and enjoy.
