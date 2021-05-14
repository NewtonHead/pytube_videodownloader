from pytube import YouTube

url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ&t=1s'
yt = YouTube(url)

video = [yt.streams.filter(file_extension='mp4', res='144p'),
        yt.streams.filter(file_extension='mp4', res='240p'),
        yt.streams.filter(file_extension='mp4', res='360p'),
        yt.streams.filter(file_extension='mp4', res='480p'),
        yt.streams.filter(file_extension='mp4', res='720p'),
        yt.streams.filter(file_extension='mp4', res='720p', fps=60),
        yt.streams.filter(file_extension='mp4', res='1080p'),
        yt.streams.filter(file_extension='mp4', res='1080p', fps=60),
        yt.streams.filter(file_extension='mp4', res='1440p'),
        yt.streams.filter(file_extension='mp4', res='2160p')]

def available_resolutions(video):
    resolutions = []
    if len(video[0]) > 0:
        resolutions.append('144p')
    if len(video[1]) > 0:
        resolutions.append('240p')
    if len(video[2]) > 0:
        resolutions.append('360p')
    if len(video[3]) > 0:
        resolutions.append('480p')
    if len(video[4]) > 0:
        if video[4] != video[5]:
            resolutions.append('720p')
    if len(video[5]) > 0:
        resolutions.append('720p60fps')
    if len(video[6]) > 0:
        if video[6] != video[7]:
            resolutions.append('1080p')
    if len(video[7]) > 0:
        resolutions.append('1080p60fps')
    if len(video[8]) > 0:
        resolutions.append('1440p')
    if len(video[9]) > 0:
        resolutions.append('2160p')
    return resolutions

resolutions = available_resolutions(video)

for i in range(0, len(resolutions)):
    print(resolutions[i])

choice = input('Which resolution you wish to download?: ')

if choice not in resolutions:
    print('Resolution not available!')
else:
    video[resolutions.index(choice)][0].download()











