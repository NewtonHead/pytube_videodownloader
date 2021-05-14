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
        resolutions.append('720p')
    if len(video[5]) > 0:
        resolutions.append('720p60fps')
    if len(video[6]) > 0:
        resolutions.append('1080p')
    if len(video[7]) > 0:
        resolutions.append('1080p60fps')
    if len(video[8]) > 0:
        resolutions.append('1440p')
    if len(video[9]) > 0:
        resolutions.append('2160p')
    return resolutions
