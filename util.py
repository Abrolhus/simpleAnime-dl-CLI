import tempfile
# EXTM3U
# #EXTINF:123, Sample artist - Sample title
# https://cdn.twist.moe/anime/yakusokunoneverlands2/[SubsPlease] Yakusoku no Neverland S2 - 01 (1080p) [D1AA4F5C].mp4


def makePlaylist(animeList, file):
        file.write('#EXTM3U\n\n')
        for anime in animeList:
            title = f'{animeList.title} - Episode {anime.ep_no}'
            file.write('#EXTINF:123, {}'.format(title) + '\n' + 'ffmpeg://' + anime.source().stream_url +'\n')


def addAnimesToPlaylist(animeList, file):
        # tf.write('#EXTM3U\n\n')
        for anime in animeList:
            title = f'{animeList.title} - Episode {anime.ep_no}'
            file.write('#EXTINF:123, {}'.format(title) + '\n' + 'ffmpeg://' + anime.source().stream_url +'\n')
