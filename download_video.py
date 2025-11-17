import yt_dlp

videos = [
    {"url": "put_the_URL_here", "title": "type_the_title_here"},
]

download_folder = "./folder/goes/here" 

for video in videos:
    url = video["url"] 

    opts = {
        'outtmpl': f"{download_folder}/{video['title']}.mp3",  
        'format': 'bestaudio/best',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")