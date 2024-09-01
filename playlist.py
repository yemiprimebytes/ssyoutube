
from pytubefix import Playlist
from pytubefix.cli import on_progress
 
url = "url"

pl = Playlist(url)

for video in pl.videos:
    ys = video.streams.get_audio_only()
    # remove mp3=True to download videos.
    ys.download(mp3=True, output_path="Downloads/")
