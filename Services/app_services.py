import os
from pytube import YouTube
from tkinter.filedialog import askdirectory
import youtube_dl
from threading import Thread as th
import sqlite3

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

class Services:
    def __init__(self):
        pass

    def getPath(self):
        folderPath = askdirectory()
        return folderPath
        
    folderPath = getPath

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
            video.download(self.folderPath())
            self.saveToDb(yt.title, yt.thumbnail_url, url)
            return True
        
    
    #Function to get user's folder path as a string
    
    
    def audio_download(self, url):
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        with ydl:
            
            audio = yt.streams.filter(only_audio=True).first()

            download_file = audio.download(self.folderPath())

            base, ext = os.path.splitext(download_file)

            new_file = base + '.mp3'
            
            os.rename(download_file, new_file)

            self.saveToDb(yt.title, yt.thumbnail_url, url)

            return True
            # Random


class ThreadHandler(th):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        th.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
        return self._return
    def join(self, *args):
        super().join(*args)
        return self._return

class Threads:
  
    def __init__(self):
        self.service = Services()

    def VideoThread(self, url):
       
        x = ThreadHandler(target=self.service.video_download,
                      
                      args=(url, ))
        
        return x.run()

    def AudioThread(self, url):
        y = ThreadHandler(target=self.service.audio_download,
                      
                      args=(url, ))
        return y.run()
        
