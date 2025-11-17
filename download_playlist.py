import yt_dlp 

playlist_url = 'https://youtube.com/playlist?list=LINK'  # your playlist goes here
download_folder = './musics'  # folder where the videos will be saved

opts = {
    'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
    }],
    'noplaylist': False,
    'ignoreerrors': True,  # continues even if an error ocurrs
    'skip_unavailable_fragments': True,  
    'download_archive': 'baixados.txt',  # save the videos already downloaded
    'quiet': False,  # show the progres on the console
}

try:
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([playlist_url])
except Exception as e:
    print(f"Erro geral: {e}")
