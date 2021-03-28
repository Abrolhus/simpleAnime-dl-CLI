import click
from Crypto.Cipher import AES
import base64
from hashlib import md5
import warnings
import requests_cache
import requests
import logging
import subprocess
import tempfile

from anime_downloader.sites import get_anime_class
import util


@click.command()
@click.argument('name')
@click.option('-e', '--ep', default=1, help='episode')
@click.option('--provider', default='twist.moe', help='site to get animes from')
@click.option('--autoplay', is_flag=True, help='Autoplays next episode')
def hello(name, ep, provider, autoplay):
    Anime = get_anime_class(provider)
    player = 'mpv'
    searchResults = Anime.search(name)
    # click.echo(searchResults)
    anime = Anime(searchResults[0].url)
    print(anime)

    episode = anime[ep-1]
    episode2 = anime[ep]
    click.echo(episode.source().stream_url)
    #click.echo(episode2.source().stream_url)
    click.echo(episode.source().referer)
    # util.play_episode(episode, player=player, title=f'{anime.title} - Episode {episode.ep_no}')
    # title=f'{anime.title} - Episode {episode.ep_no}'
    # title2=f'{anime.title} - Episode {episode2.ep_no}'
        # p = subprocess.Popen([
            # player,
            # '--title={}'.format(title),
            # '--referrer="{}"'.format(episode.source().referer),
            # episode.source().stream_url,
            # '--title={}'.format(title2),
            # '--referrer="{}"'.format(episode2.source().referer),
            # episode2.source().stream_url
        # ])
    tfile = tempfile.NamedTemporaryFile(mode='a+', suffix='.m3u8')
    mpvArgs = [player, '--referrer={}'.format('https://twist.moe/'), '--playlist']
    if player == 'mpv':
        util.makePlaylist(anime[0:1], tfile)
        # for epi in anime:
        # title = f'{anime.title} - Episode {epi.ep_no}'
        # mpvArgs += ['--title={}'.format(title),
        # 'ffmpeg://{}'.format(epi.source().stream_url)]
        # click.echo("uai")
        print(tfile.name)
        mpvArgs.append(tfile.name)
        print(mpvArgs)
        tfile.seek(0)
        print(tfile.read())
        #mpvArgs.append('{0} >/dev/null 2>&1 &')
        #subprocess.Popen("nohup usr/local/bin/otherscript.pl {0} >/dev/null 2>&1 &", shell=True)
        print(''.join(mpvArgs))
        p = subprocess.Popen(mpvArgs)
        p.wait()
        util.addAnimesToPlaylist(anime[1:], tfile)
        print("humm")
        print(anime[0:1])
        print(anime[1:])
        print("uaaaaaaaaaaaaaaaaaaaaaaaa");
    else:
        p = subprocess.Popen([player, episode.source().stream_url])
        p.wait()

if __name__ == "__main__":
    hello()
