If python3 is not currently installed download at: https://www.python.org/downloads/ (Not Necessary on linux, install via repositories.)

On Windows
1) Run the Installer file
2) Select the "Customize installation" option
3) Be sure to check the pip, tcl/tk and py launcher options in the installer.
4) Check the Associate files with python, Create shortcuts, add Python to environment variables, and precompile library check boxes.

On Linux
1) Install python, python-pip, python-tk, python3, python3-pip, python3-tk

Once python3 has installed open your terminal: Windows win+r: cmd <Enter>
Once in the terminal, type the following: python -m pip install --upgrade pip # this updates pip to the latest version
When that completes type the following: pip install --upgrade youtube_dl # This installs the lates version of youtube-dl

Now that python and youtube_dl are installed, it is time to download ffmpeg. (not Necessary on linux since you can install via repositories.)

On Windows
1) Go to: https://ffmpeg.org/download.html
2) Once you download your respective version of ffmpeg, extract it.
3) Note the location of the ffmpeg.exe file and paste it in the YoutubeDL.py file under the #Variables (line #129) line in the quotes of the ffmpeg_location variable.
*Be sure that there is only a single pair of quotations*

On Linux
1) Install ffmpeg with your package manager.
2) type: whereis ffmpeg | awk {'print $2'} *this shows the location of ffmpeg*
3) Note the location of the ffmpeg file

Save the YouTubeDL.py file and enjoy.
