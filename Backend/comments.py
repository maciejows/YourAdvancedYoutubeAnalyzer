import os
import threading
import requests


class Com:

    def __init__(self, url):
        self.komentarze = []
        self.vidID = url

    def down(self):
        r2 = requests.get(
            'https://www.googleapis.com/youtube/v3/commentThreads?key=' + os.environ[
                'APIKEY'] + '&textFormat=plainText&part=snippet&videoId=' + self.vidID + '&maxResults=100')
        komenty = r2.json()
        self.komentarze.extend(komenty['items'])
        if 'nextPageToken' in komenty:
            threading.Thread(target=self.downn(ext=komenty['nextPageToken'])).start()

    def downn(self, ext):
        r2 = requests.get(
            'https://www.googleapis.com/youtube/v3/commentThreads?key=' + os.environ[
                'APIKEY'] + '&textFormat=plainText&part=snippet&videoId=' + self.vidID + '&maxResults=100'
            + '&pageToken=' + ext)
        komenty = r2.json()
        self.komentarze.extend(komenty['items'])
        if 'nextPageToken' in komenty:
            threading.Thread(target=self.downn(ext=komenty['nextPageToken'])).start()