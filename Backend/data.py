import json
import os
import time
from collections import Counter

import requests
import youtube_dl
from youtube_api import YouTubeDataAPI

ydl_opts = {
    'format': '160',
    'outtmpl': '/%(id)s.%(ext)s'
}


class Data:

    def __init__(self, url, bool):
        print(url)
        with youtube_dl.YoutubeDL(ydl_opts) as yt:
            jsonmovie = yt.extract_info(url, download=bool)
        print(jsonmovie)
        self.vidTitle = jsonmovie["title"]
        self.vidThumbnail = jsonmovie["thumbnail"]
        self.vidID = jsonmovie["id"]
        self.vidWebUrl = jsonmovie["webpage_url"]
        self.vidCommentCount = "56465678"
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
        self.chanName = self.jsonmovie2["items"][0]["snippet"]["title"]
        self.chanWebUrl = "https://www.youtube.com/channel/" + self.chanID
        self.chanViewCount = self.jsonmovie2["items"][0]["statistics"]["viewCount"]
        self.chanSubscriberCount = self.jsonmovie2["items"][0]["statistics"]["subscriberCount"]
        self.chanVideoCount = self.jsonmovie2["items"][0]["statistics"]["videoCount"]
        self.chanPublishedAt = self.jsonmovie2["items"][0]["snippet"]["publishedAt"]
        self.data = {"videoTitle": self.vidTitle, "thumbnailURL": self.vidThumbnail, "videoId": self.vidID,
                     "videoUrl": self.vidWebUrl, "tags": self.vidTags,
                     "videoUploader": self.vidUploader, "videoCategories": self.vidCategories,
                     "ageLimit": self.vidAgeLimit, "videoViewCount": self.vidViewCount,
                     "videoDislikeCount": self.vidDislikeCount, ''''"commentsCount": self.vidCommentCount,'''
                     "videoLikeCount": self.vidLikeCount, "videoAverageRating": self.vidAverageRating,
                     "videoDuration": self.vidDuration, "channelId": self.chanID, "channelName": self.chanName,
                     "channelUrl":self.chanWebUrl, "channelTotalVideoViews": self.chanViewCount,
                     "subscribersNumber": self.chanSubscriberCount, "videosNumber": self.chanVideoCount,
                     "channelPublishedAt": self.chanPublishedAt}

    def getContent(self):
        return (self.data)