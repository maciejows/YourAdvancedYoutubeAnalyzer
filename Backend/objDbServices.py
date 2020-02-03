# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, String, Text, create_engine, MetaData, Table
from sqlalchemy.dialects.mysql import BIGINT, MEDIUMINT


class objDB():
    metadata = MetaData()
    engine = create_engine(
        "mysql://root:lubiemaslo@youtubeanalyzer.cqmx3x4uk8ob.us-east-1.rds.amazonaws.com:3306/yayaDB", echo=True)

    channels = Table(
        'channels', metadata,
        Column('channelID', String(255), primary_key=True, unique=True),
        Column('channelName', Text),
        Column('channelUrl', Text),
        Column('subscriberCount', BIGINT(20)),
        Column('viewsCount', BIGINT(20)),
        Column('publishedAt', Date),
        Column('videosCount', MEDIUMINT),
    )

    videos = Table(
        'videos', metadata,
        Column('videoID', String(255), primary_key=True, unique=True),
        Column('channelID', ForeignKey('channels.channelID'), index=True),
        Column('videoTitle', Text),
        Column('videoUrl', Text),
        Column('thumbnailUrl', Text),
        Column('categories', Text),
        Column('tags', Text),
        Column('uploader', Text),
        Column('comments', MEDIUMINT),
        Column('views', MEDIUMINT),
        Column('ageLimit', MEDIUMINT),
        Column('rating', Float(asdecimal=True)),
        Column('likes', MEDIUMINT),
        Column('dislikes', MEDIUMINT),
        Column('duration', MEDIUMINT),
        Column('histogram', Text),
    )

    def getTables(self):
        connect = self.engine.connect()
        data = self.engine.table_names()
        connect.close()
        return data

    def getHist(self, vidID):
        s = self.videos.select(self.videos.histogram).where(self.videos.c.videoID == vidID)
        connect = self.engine.connect()
        result = connect.execute(s)
        connect.close()
        #print(result)
        #return result.fetchone()

    def getVideoData(self, vidID):
        s = self.videos.select().where(self.videos.c.videoID == vidID)
        connect = self.engine.connect()
        result = connect.execute(s)
        #print(result)
        res = result.fetchone()
        connect.close()
        return res

    def getChannelData(self, channelID):
        s = self.channels.select().where(self.channels.c.channelID == channelID)
        connect = self.engine.connect()
        result = connect.execute(s)
        #print(result)
        res = result.fetchone()
        #print(res)
        connect.close()
        return res

    def getData(self, vidID):
        if self.ifVideo(vidID):
            vidQuery = self.getVideoData(vidID)
            if self.ifChannel(vidQuery[1]):
                chanQuery = self.getChannelData(vidQuery[1])
#                print(vidQuery + chanQuery)
                query = {"videoId": vidQuery[0], "videoTitle": vidQuery[2], "videoUrl": vidQuery[3],
                         "thumbnailURL": vidQuery[4], "videoCategories": vidQuery[5], "tags": vidQuery[6],
                         "videoUploader": vidQuery[7], "commentsCount": vidQuery[8],
                         "videoViewCount": vidQuery[9], "ageLimit": vidQuery[10], "videoAverageRating": vidQuery[11],
                         "videoLikeCount": vidQuery[12], "videoDislikeCount": vidQuery[13],
                         "videoDuration": vidQuery[14],
                         "channelId": chanQuery[0], "channelName": chanQuery[1],
                         "channelUrl": chanQuery[2], "subscribersNumber": chanQuery[3],
                         "channelTotalVideoViews": chanQuery[4], "channelPublishedAt": chanQuery[5],
                         "videosNumber": chanQuery[6]}
                return query
            else:
                print("No such data in the database.")

    def addHist(self, vidID, hist):
        if self.ifVideo(vidID):
            updt = self.videos.update().where(self.videos.c.videoID == vidID).values(histogram=hist)
            connect = self.engine.connect()
            result = connect.execute(updt)
            #res = result.fetchone()
            #print(res)
            connect.close()

    def addData(self, dbData):
        # Checking if channel is in database. If it is, updating data
        if self.ifChannel(dbData.chanID):
            ins = self.channels.update().values(subscriberCount=dbData.chanSubscriberCount,
                                                viewsCount=dbData.chanViewCount, videosCount=dbData.chanVideoCount)
        else:
            ins = self.channels.insert().values(channelID=dbData.chanID, channelName=dbData.chanName,
                                                channelUrl=dbData.chanWebUrl,
                                                subscriberCount=dbData.chanSubscriberCount,
                                                viewsCount=dbData.chanViewCount, publishedAt=dbData.chanPublishedAt,
                                                videosCount=dbData.chanVideoCount)
        # Checking if video is in database. If it is, updating data
        connect = self.engine.connect()
        result = connect.execute(ins)
        #res = result.fetchone()
        #print(res)
        connect.close()
        if self.ifVideo(dbData.vidID):
            ins = self.videos.update().values(comments=dbData.vidCommentCount, views=dbData.vidViewCount,
                                              rating=dbData.vidAverageRating, likes=dbData.vidLikeCount,
                                              dislikes=dbData.vidDislikeCount)

        else:
            # Adding new record to the videos Table if video is not present in database
            ins = self.videos.insert().values(videoID=dbData.vidID, channelID=dbData.chanID, videoTitle=dbData.vidTitle,
                                              videoUrl=dbData.vidWebUrl, thumbnailUrl=dbData.vidThumbnail,
                                              categories=str(dbData.vidCategories)[1:][:-1],
                                              tags=str(dbData.vidTags)[1:][:-1], uploader=dbData.vidUploader,
                                              comments=dbData.vidCommentCount,
                                              views=dbData.vidViewCount, ageLimit=dbData.vidAgeLimit,
                                              rating=dbData.vidAverageRating, likes=dbData.vidLikeCount,
                                              dislikes=dbData.vidDislikeCount, duration=dbData.vidDuration)
        connect = self.engine.connect()
        result = connect.execute(ins)
        #res = result.fetchone()
        #print(res)
        connect.close()

    def ifVideo(self, videoID):
        s = self.videos.select().where(self.videos.c.videoID == videoID)
        connect = self.engine.connect()
        result = connect.execute(s)
        res = result.fetchone()
        connect.close()
        #print("ifVideos " + str(res))
        if str(res) == "None":
            print("No such video in the database.")
            return False
        else:
            return True

    def ifHist(self, videoID):
        s = self.videos.select(self.videos.c.histogram).where(self.videos.c.videoID == videoID)
        connect = self.engine.connect()
        result = connect.execute(s)
        res = result.fetchone()
        connect.close()
        #print("ifHist: " + str(res))
        if str(res) == "None" or str(res) == "NULL":
            print("No such histogram in the database.")
            return False
        else:
            return True

    def ifChannel(self, chanID):
        s = self.channels.select().where(self.channels.c.channelID == chanID)
        connect = self.engine.connect()
        result = connect.execute(s)
        res = result.fetchone()
        connect.close()
        #print("ifChannel " + str(res))
        if str(res) == "None":
            print("No such channel in the database.")
            return False
        return True
