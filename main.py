from pytube import YouTube
from func import available_resolutions
import os

url = input('Enter video url: ')
yt = YouTube(url)

which = input('mp4 or mp3?: ')

if which == 'mp4':

    video = [yt.streams.filter(file_extension='mp4', res='144p').first(),
            yt.streams.filter(file_extension='mp4', res='240p').first(),
            yt.streams.filter(file_extension='mp4', res='360p').first(),
            yt.streams.filter(file_extension='mp4', res='480p').first(),
            yt.streams.filter(file_extension='mp4', res='720p').first(),
            yt.streams.filter(file_extension='mp4', res='720p', fps=60).first(),
            yt.streams.filter(file_extension='mp4', res='1080p').first(),
            yt.streams.filter(file_extension='mp4', res='1080p', fps=60).first(),
            yt.streams.filter(file_extension='mp4', res='1440p').first(),
            yt.streams.filter(file_extension='mp4', res='2160p').first()]

    resolutions = available_resolutions(video)

    for i in range(0, len(resolutions)):
        print(resolutions[i])

    choice = input('Which resolution you wish to download?: ')

    if choice not in resolutions:
        print('Invalid input!')
    else:
        destination = '/home/user/pythonprojects/pythontube/downloads/video'
        video[resolutions.index(choice)].download(output_path=destination)
        print('Download succesfull, saved on ' + destination)

elif which == 'mp3':
    audio = yt.streams.filter(only_audio=True).first()
    destination = '/home/user/pythonprojects/pythontube/downloads/audio'
    out_file = audio.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print('Download succesfull, saved on ' + destination)












