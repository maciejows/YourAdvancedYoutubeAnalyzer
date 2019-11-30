import os
import requests
import youtube_dl

ydl_opts = {
    'format': '160',
    'outtmpl': '/%(id)s.%(ext)s'
}


class Data:
    # TODO 0: create default constructor with no parameters
    '''def __init__(self):
        self.vidTitle = ""
        self.vidThumbnail = ""
        self.vidID = ""
        self.vidWebUrl = ""
        self.vidCommentCount = 0
        self.vidTags = ""
        self.vidUploader = ""
        self.vidCategories = ""
        self.vidAgeLimit = 0
        self.vidViewCount = 0
        self.vidDislikeCount = 0
        self.vidLikeCount = 0
        self.vidAverageRating = 0.0
        self.vidDuration = 0
        self.chanID = ""
        self.chanName = "TEMP NAME"
        self.chanWebUrl = "TEMP NAME"
        self.chanViewCount = 0
        self.chanSubscriberCount = 0
        self.chanVideoCount = 0
        self.chanPublishedAt = ""'''

    def __init__(self, url, bool):
        with youtube_dl.YoutubeDL(ydl_opts) as yt:
            jsonmovie = yt.extract_info(url, download=bool)
        print(jsonmovie)
        self.vidTitle = jsonmovie["title"]
        self.vidThumbnail = jsonmovie["thumbnail"]
        self.vidID = jsonmovie["id"]
        self.vidWebUrl = jsonmovie["webpage_url"]
        # TODO 1: add comment count jsonmovie
        self.vidCommentCount = jsonmovie[""]
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
        # TODO 2: add channel name and channel URL
        self.chanName = "TEMP NAME"
        self.chanWebUrl = "TEMP NAME"
        self.chanViewCount = self.jsonmovie2["items"][0]["statistics"]["viewCount"]
        # !!Commented chanCommentCount!!
        # self.chanCommentCount = self.jsonmovie2["items"][0]["statistics"]["commentCount"] "ilosc_komentarzy_kanalu":self.chanCommentCount,
        self.chanSubscriberCount = self.jsonmovie2["items"][0]["statistics"]["subscriberCount"]
        self.chanVideoCount = self.jsonmovie2["items"][0]["statistics"]["videoCount"]
        self.chanPublishedAt = self.jsonmovie2["items"][0]["snippet"]["publishedAt"]
        self.data = {"tytul": self.vidTitle, "thumbnail": self.vidThumbnail, "id": self.vidID,
                     "url_strony": self.vidWebUrl, "tagi": self.vidTags,
                     "Uploadujacy": self.vidUploader, "Kategorie": self.vidCategories,
                     "ograniczenie_wiekowe": self.vidAgeLimit, "ilosc_wyswietlen": self.vidViewCount,
                     "ilosc_dislikeow": self.vidDislikeCount,
                     "ilosc_likeow": self.vidLikeCount, "srednia_ocena": self.vidAverageRating,
                     "dlugosc_filmu": self.vidDuration, 'id_kanalu': self.chanID,
                     "ilosc_wys_film_kanal: ": self.chanViewCount,
                     "ilosc_subskrybentow": self.chanSubscriberCount, "ilosc_filmu": self.chanVideoCount,
                     "publikacja_kanalu": self.chanPublishedAt}

    def getContent(self):
        return (self.data)
