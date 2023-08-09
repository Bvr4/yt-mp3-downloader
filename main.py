import os
import subprocess
from pytube import YouTube
from pytube import Playlist


# vérifier urls
def verify_urls(urls_in):
    BASE_YOUTUBE_URL = "https://www.youtube.com/"
    BASE_YOUTUBE_URL_SHORTENED = "https://youtu.be/"
    urls_out = []

    for url in urls_in:
        if url.lower().startswith(BASE_YOUTUBE_URL) or url.lower().startswith(BASE_YOUTUBE_URL_SHORTENED):
            urls_out.append(url)
        else:
            print('url incorrecte : ' + url)

    return urls_out


def read_input_file(file_name):
    content = []

    with open(file_name, "r") as input_file:
        for line in input_file:
            line = line.rstrip()
            content.append(line)
    
    return content


def convert_to_mp3(audio_file_name):
    audio_title = '.'.join(audio_file_name.split('.')[:-1]) # pour retirer l'extension du file name

    # Conversion du fichier en mp3
    command = 'ffmpeg -i "' + audio_file_name + '" -q:a 0 "' + audio_title + '".mp3'
    subprocess.run(command, shell=True)

    # Suppression du fichier audio original
    os.remove(audio_file_name)


def get_best_audio_stream(yt_url):
    youtube_video = YouTube(yt_url)
    best_audio_stream = youtube_video.streams.filter(only_audio=True).order_by('abr').last() # on filtre par type et par meilleur bitrate
    # print(best_audio_stream)
    itag = best_audio_stream.itag
    return youtube_video.streams.get_by_itag(itag)


# lecture des urls des vidéos
urls = read_input_file("url_videos_a_telecharger.txt")

# lecture des urls des playlists
playlist_urls = read_input_file("url_playlist_a_telecharger.txt")

# Pour chaque playlist on va chercher les url des vidéos qui composent la playlist
for playlist_url in playlist_urls:
    print(playlist_url)
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        urls.append(video_url)

urls = verify_urls(urls)

for url in urls:
    # téléchargement du fichier audio
    stream = get_best_audio_stream(url)
    stream.download()

    convert_to_mp3(stream.default_filename)

