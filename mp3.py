# Extract MP3 from Youtube Video.
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "url"

yt = YouTube(url, on_progress_callback = on_progress)
print(f"{yt.title}  -- Downloaded")

ys = yt.streams.get_audio_only()
ys.download(mp3=True, output_path="Downloads/")