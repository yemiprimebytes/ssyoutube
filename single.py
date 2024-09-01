from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=2b_KfAGiglc"
 
yt = YouTube(url, on_progress_callback = on_progress)
print(f"Downloading - {yt.title}")

ys = yt.streams.get_highest_resolution()
ys.download(output_path="Downloads/")