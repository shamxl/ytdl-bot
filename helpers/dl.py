from pytube import YouTube 
import io


async def download (url):

    buffer = io.BytesIO()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    buffer.name = video.title
    video.stream_to_buffer(buffer)
    
    return buffer

    
