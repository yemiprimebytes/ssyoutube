
from pytubefix import Playlist
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=jqCo89XFEoc&list=OLAK5uy_mo8OCMdAkRJtBRYgupsCD71RWsmNIJTUU"
url = "https://www.youtube.com/watch?v=qSIOp_K5GMw&list=RDQMbO4w_MU_6r8&index=2"

pl = Playlist(url)
print("Downloading...") 

for video in pl.videos:
    ys = video.streams.get_audio_only()
    # remove mp3=True to download videos.
    ys.download(mp3=True, output_path="Downloads/")
