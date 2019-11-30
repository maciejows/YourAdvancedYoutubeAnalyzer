import os
import requests
import youtube_dl

ydl_opts = {
    'format':'160',
    'outtmpl': '/%(id)s.%(ext)s'
}

class Data:
    def __init__(self,url,bool):
        with youtube_dl.YoutubeDL(ydl_opts) as yt:
            jsonmovie = yt.extract_info(url, download=bool)
        print(jsonmovie)
        self.vidTitle = jsonmovie["title"]
        self.vidThumbnail = jsonmovie["thumbnail"]
        self.vidID = jsonmovie["id"]
        self.vidWebUrl = jsonmovie["webpage_url"]
        self.vidTags = jsonmovie["tags"]
        self.vidUploader = jsonmovie["uploader"]
        self.vidCategories = jsonmovie["categories"]
        self.vidAgeLimit = jsonmovie["age_limit"]
        self.vidViewCount = jsonmovie["view_count"]
        self.vidDislikeCount = jsonmovie["dislike_count"]
        self.vidLikeCount = jsonmovie["like_count"]
        self.vidAverageRating = jsonmovie["average_rating"]
        self.vidDuration = jsonmovie["duration"]
        self.chanID = jsonmovie['channel_id']
        r = requests.get(
            'https://www.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id=' +
            self.chanID + '&key=' + os.environ['APIKEY'])
        self.jsonmovie2 = r.json()
        self.chanViewCount = self.jsonmovie2["items"][0]["statistics"]["viewCount"]
        self.chanCommentCount = self.jsonmovie2["items"][0]["statistics"]["commentCount"]
        self.chanSubscriberCount = self.jsonmovie2["items"][0]["statistics"]["subscriberCount"]
        self.chanVideoCount = self.jsonmovie2["items"][0]["statistics"]["videoCount"]
        self.chanPublishedAt = self.jsonmovie2["items"][0]["snippet"]["publishedAt"]
        self.data = {"tytul":self.vidTitle, "thumbnail": self.vidThumbnail, "id": self.vidID, "url_strony": self.vidWebUrl, "tagi": self.vidTags,
                    "Uploadujacy": self.vidUploader, "Kategorie": self.vidCategories,
                    "ograniczenie_wiekowe": self.vidAgeLimit, "ilosc_wyswietlen": self.vidViewCount, "ilosc_dislikeow": self.vidDislikeCount,
                     "ilosc_likeow": self.vidLikeCount,"srednia_ocena": self.vidAverageRating,
                     "dlugosc_filmu": self.vidDuration, 'id_kanalu': self.chanID, "ilosc_wys_film_kanal: ": self.chanViewCount,"ilosc_komentarzy_kanalu":self.chanCommentCount,
                     "ilosc_subskrybentow": self.chanSubscriberCount, "ilosc_filmu":self.chanVideoCount,"publikacja_kanalu":self.chanPublishedAt}

    def getContent(self):
        return (self.data)