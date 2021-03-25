import click
from Crypto.Cipher import AES
import base64
from hashlib import md5
import warnings
import requests_cache
import requests
import logging
import subprocess

from anime_downloader.sites import get_anime_class


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
    click.echo(episode.source().referer)
    # util.play_episode(episode, player=player, title=f'{anime.title} - Episode {episode.ep_no}')
    # title=f'{anime.title} - Episode {episode.ep_no}'
    # title2=f'{anime.title} - Episode {episode2.ep_no}'
    if player == 'mpv':
        # p = subprocess.Popen([
            # player,
            # '--title={}'.format(title),
            # '--referrer="{}"'.format(episode.source().referer),
            # episode.source().stream_url,
            # '--title={}'.format(title2),
            # '--referrer="{}"'.format(episode2.source().referer),
            # episode2.source().stream_url
        # ])
        mpvArgs = [player]
        for epi in anime:
            title = f'{anime.title} - Episode {epi.ep_no}'
            mpvArgs += ['--title={}'.format(title),
            '--referrer="{}"'.format(epi.source().referer),
            epi.source().stream_url]
            click.echo("uai");
        p = subprocess.Popen(mpvArgs)
    else:
        p = subprocess.Popen([player, episode.source().stream_url
                              ])
    p.wait()

if __name__ == "__main__":
    hello()
