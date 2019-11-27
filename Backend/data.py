import os
import requests
import youtube_dl

ydl_opts = {
    'format':'160',
    'outtmpl': '/%(id)s.%(ext)s'
}

class Data:
    def __init__(self,url):
        with youtube_dl.YoutubeDL(ydl_opts) as yt:
            jsonmovie = yt.extract_info(url, download=True)
        print(jsonmovie)
        self.title = jsonmovie["title"]
        self.thumbnail = jsonmovie["thumbnail"]
        self.id = jsonmovie["id"]
        self.webpage_url = jsonmovie["webpage_url"]
        self.tags = jsonmovie["tags"]
        self.uploader = jsonmovie["uploader"]
        self.categories = jsonmovie["categories"]
        self.age_limit = jsonmovie["age_limit"]
        self.view_count = jsonmovie["view_count"]
        self.dislike_count = jsonmovie["dislike_count"]
        self.like_count = jsonmovie["like_count"]
        self.average_rating = jsonmovie["average_rating"]
        self.duration = jsonmovie["duration"]
        self.channel_id = jsonmovie['channel_id']
        r = requests.get(
            'https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id=' +
            self.channel_id + '&key=' + os.environ['APIKEY'])
        self.jsonmovie2 = r.json()
        self.viewCount = self.jsonmovie2["items"][0]["statistics"]["viewCount"]
        self.commentCount = self.jsonmovie2["items"][0]["statistics"]["commentCount"]
        self.subscriberCount = self.jsonmovie2["items"][0]["statistics"]["subscriberCount"]
        self.videoCount = self.jsonmovie2["items"][0]["statistics"]["videoCount"]
        self.publishedAt = self.jsonmovie2["items"][0]["snippet"]["publishedAt"]
        self.data = {"tytul":self.title, "thumbnail": self.thumbnail, "id": self.id, "url_strony": self.webpage_url, "tagi": self.tags,
                    "Uploadujacy": self.uploader, "Kategorie": self.categories,
                    "ograniczenie_wiekowe": self.age_limit, "ilosc_wyswietlen": self.view_count, "ilosc_dislikeow": self.dislike_count,
                     "ilosc_likeow": self.like_count,"srednia_ocena": self.average_rating,
                     "dlugosc_filmu": self.duration, 'id_kanalu': self.channel_id,"ilosc_komentarzy_kanalu":self.commentCount,
                     "ilosc_subskrybentow": self.subscriberCount, "ilosc_filmu":self.videoCount,"publikacja_kanalu":self.videoCount}

    def pobierz_dane(self):
        print(self.jsonmovie2)
        return (self.data)