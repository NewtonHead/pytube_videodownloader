def available_resolutions(video):
    resolutions = []
    if video[0] != None:
        resolutions.append('144p')
    if video[1] != None:
        resolutions.append('240p')
    if video[2] != None:
        resolutions.append('360p')
    if video[3] != None:
        resolutions.append('480p')
    if video[4] != None:
        resolutions.append('720p')
    if video[5] != None:
        resolutions.append('720p60fps')
    if video[6] != None:
        resolutions.append('1080p')
    if video[7] != None:
        resolutions.append('1080p60fps')
    if video[8] != None:
        resolutions.append('1440p')
    if video[9] != None:
        resolutions.append('2160p')
    return resolutions
