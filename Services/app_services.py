import os
from pytube import YouTube
from tkinter.filedialog import askdirectory
import youtube_dl
import threading as th
import sqlite3

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

class Services:
    def _init_(self):
        pass

    def saveToDb(self, videoTitle, videoThumbnail, videoUrl):
        conn = sqlite3.connect(os.path.realpath('../env/db/info.db'))
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS videos (url TEXT, title TEXT, thumbnail TEXT)")
        cursor.execute("INSERT INTO videos (url, title, thumbnail) VALUES (?, ?, ?)", (videoUrl, videoTitle, videoThumbnail))
        conn.commit()
        conn.close()

    def video_download(self, url):
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        with ydl:
            video = yt.streams.get_highest_resolution()
            video.download()
            self.saveToDb(yt.title, yt.thumbnail_url, url)
    
    #Function to get user's folder path as a string
    def getPath(self):
        folderPath = askdirectory()
        return folderPath
        
    folderPath = getPath
    
    def audio_download(self, url):
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        with ydl:
            
            audio = yt.streams.filter(only_audio=True).first()

            download_file = audio.download(self.folderPath())

            base, ext = os.path.splitext(download_file)

            new_file = base + '.mp3'
            
            os.rename(download_file, new_file)

            self.saveToDb(yt.title, yt.thumbnail_url, url)
            # Random




class Threads:
    def _init_(self):
        self.service = Services()

    def VideoThread(self, url):
        x = th.Thread(target=self.service.video_download,
                      daemon=True,
                      args=(url, ))
        x.start()

    def AudioThread(self, url):
        y = th.Thread(target=self.service.audio_download,
                      daemon=True,
                      args=(url, ))
        y.start()