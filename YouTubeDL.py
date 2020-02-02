import youtube_dl
import os
import sys
from tkinter import *
import tkinter.messagebox as mb
from tkinter import filedialog as fd



def get_url():
    if (browse_var.get() and extract_var.get()):
        full_path = fd.asksaveasfilename()
        split_path = os.path.split(full_path)
        os.chdir(split_path[0])
        if keep_var.get():
            ytdl_opts = {
                        'keepvideo': True,
                        'ffmpeg_location': ffmpeg_location,
                        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': formats_var.get()}],
                        'outtmpl': split_path[1] + '.%(ext)s'
                        }
        else:
            ytdl_opts = {
                        'ffmpeg_location': ffmpeg_location,
                        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': formats_var.get()}],
                        'outtmpl': split_path[1] + '.%(ext)s'
                        }
        with youtube_dl.YoutubeDL(ytdl_opts) as yt:
            yt.download([url_enter.get()])
    elif extract_var.get() and play_var.get():
        os.chdir(fd.askdirectory())
        if keep_var.get():
            ytdl_opts = {
                         'keepvideo': True,
                         'ffmpeg_location': ffmpeg_location,
                         'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': formats_var.get()}],
                         'outtmpl': '%(title)s.%(ext)s'
                         }
        else:
            ytdl_opts = {
                         'ffmpeg_location': ffmpeg_location,
                         'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': formats_var.get()}],
                         'outtmpl': '%(title)s.%(ext)s'
                         }
        with youtube_dl.YoutubeDL(ytdl_opts) as yt:
            yt.download([url_enter.get()])
    elif browse_var.get():
        full_path = fd.asksaveasfilename()
        split_path = os.path.split(full_path)
        os.chdir(split_path[0])
        ytdl_opts = {'outtmpl': split_path[1] + '.%(ext)s'}
        with youtube_dl.YoutubeDL(ytdl_opts) as yt:
            yt.download([url_enter.get()])
    elif extract_var.get():
        
        if os.path.isdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\'):
            os.chdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\')
        else:
            os.mkdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\')
            os.chdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\')
        if keep_var.get():
            ytdl_opts = {
                         'keepvideo': True,
                         'ffmpeg_location': ffmpeg_location,
                         'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': formats_var.get()}],
                         'outtmpl': '%(title)s.%(ext)s'
                         }
        else:
            ytdl_opts = {
                         'ffmpeg_location': ffmpeg_location,
                         'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': formats_var.get()}],
                         'outtmpl': '%(title)s.%(ext)s'
                         }
        with youtube_dl.YoutubeDL(ytdl_opts) as yt:
            yt.download([url_enter.get()])
    elif play_var.get():
        os.chdir(fd.askdirectory())
        ytdl_opts = {'outtmpl': '%(title)s.%(ext)s'}
        with youtube_dl.YoutubeDL(ytdl_opts) as yt:
            yt.download([url_enter.get()])
    else:
        if os.path.isdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\'):
            os.chdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\')
        else:
            os.mkdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\')
            os.chdir(os.getenv('USERPROFILE') + '\\videos\\youtube-dl\\')
        ytdl_opts = {'outtmpl': '%(title)s.%(ext)s', 'progress_hooks': [hook_info]}
        with youtube_dl.YoutubeDL(ytdl_opts) as yt:
            yt.download([url_enter.get()])


def hook_info(d):
    
    if d['status'] == 'downloading':
        notif = Toplevel(screen)
        notif.wm_title('Downloading')
        notif_label = Label(notif, text='_percent_str')
    elif d['status'] == 'finished':
        file_tuple = os.path.split(os.path.abspath(d['filename']))
        mb.showinfo('', 'Done downloading {}'.format(file_tuple[1]))


def disable_enable_custom():
    file_name.configure(state=DISABLED if play_var.get() else NORMAL)
    browse_var.set(0)
    

def disable_enable_keep():
    keep_video.configure(state=NORMAL if extract_var.get() else DISABLED)
    formats.configure(state=NORMAL if extract_var.get() else DISABLED)


def exit_program():
    screen.destroy()
    sys.exit(0)


# Variables =
ffmpeg_location = ''

# Begin GUI
screen = Tk()
screen.title('YouTube-DL GUI')
screen.geometry('330x175')
banner = Label(screen, text='YouTube Downloader')
banner.grid(row=0, column=0, columnspan=2)

# Obtaining the URL
url_label = Label(screen, text='Enter the URL: ')
url_label.grid(row=1, column = 0, sticky=W)
url_enter = Entry(screen, width=35)
url_enter.grid(row=1, column=1, columnspan=2, sticky=W)

# Options
options = Label(screen, text='Additional Options:')
options.grid(row=3, column=0, sticky=W)

# Saving video as a custom name
browse_var = IntVar()
file_name = Checkbutton(screen, variable=browse_var, text='Save as custom name')
file_name.grid(row=3, column=1, sticky=W)

# Extract Audio
extract_var = IntVar()
keep_var = IntVar()
keep_video = Checkbutton(screen, variable=keep_var, text='Keep Video', state=DISABLED)
extract = Checkbutton(screen, variable=extract_var, text='Extract Audio', command=disable_enable_keep)
extract.grid(row=4, column=1, sticky=W)
keep_video.grid(row=5, column=1)

formats_var = StringVar()
values={'flac', 'mp3', 'aac', 'm4a', 'opus', 'vorbis', 'wav'}
formats_var.set('flac')
formats = OptionMenu(screen, formats_var, *values)
formats.configure(state=DISABLED)
formats.grid(row=4, column=2)

# Playlist
play_var = IntVar()
play_check = Checkbutton(screen, variable=play_var, text='Playlist', command=disable_enable_custom)
play_check.grid(row=6, column=1, sticky=W)
# End Options

# Execution Buttons
download = Button(screen, text='Download Video', command=get_url)
download.grid(row=7, column=0)
quit_program = Button(screen, text='Quit', command=exit_program)
quit_program.grid(row=7, column=1, sticky=W)
screen.mainloop()
# End Execution Buttons
# End GUI
