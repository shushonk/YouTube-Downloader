import yt_dlp

link = input("Enter a link to download: ")

# Use yt-dlp to download video in a single format
ydl_opts = {
    'format': 'best',  # This will choose the best available single file (audio + video in one stream)
    'outtmpl': 'Video_Download.%(ext)s',  # Save with the appropriate extension
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("Downloading....")
    ydl.download([link])
    print("Finished Downloading....")
#pip install yt-dlp