from pytube import YouTube 
import io


def download (url):

    buffer = io.BytesIO()
    yt = YouTube(url)
    yt.streams.get_highest_resolution().stream_to_buffer(buffer)

    return buffer

    
print (download("https://youtube.com/shorts/TFmMP9sDMoc?si=H25yCmYZO8N1c1XB"))
