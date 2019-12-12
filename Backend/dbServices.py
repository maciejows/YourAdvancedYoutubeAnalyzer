import os
import mysql.connector
from mysql.connector import errorcode


class ytDB:
    def __init__(self):
        try:
            self.rdsdb = mysql.connector.connect(
                user=os.environ["user"],
                passwd=os.environ["passwd"],
                host=os.environ["host"],
                database=os.environ["database"],
            )
            print("succesfully connected to the database: " + str(self.rdsdb))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Acess denied/wrong  user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
            else:
                print(err)
        else:
            self.dbCursor = self.rdsdb.cursor()

    def closeConnection(self):
        self.rdsdb.close()

    def getTables(self):
        return self.dbCursor.execute("Show tables")

    def getTable(self, tableName, records):
        if records != 0:
            query = self.dbCursor.execute("SELECT TOP " + str(records) + " * FROM " + str(tableName))
        else:
            query = self.dbCursor.execute("SELECT * FROM " + str(tableName))
        return query.fetchall()

    def getVideoData(self, vidID):
        self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '" + vidID + "'")
        return self.dbCursor.fetchone()

    def getChannelData(self, channelID):
        self.dbCursor.execute("SELECT * FROM channels WHERE channelID like '" + channelID + "'")
        return self.dbCursor.fetchone()

    def getData(self, vidID):
        if self.ifVideo(vidID):
            vidQuery = self.getVideoData(vidID)
            if self.ifChannel(vidQuery[1]):
                chanQuery = self.getChannelData(vidQuery[1])
                print(vidQuery + chanQuery)
                query = {"videoId": vidQuery[0], "videoTitle": vidQuery[2],  "videoUrl": vidQuery[3],
                         "thumbnailURL": vidQuery[4], "videoCategories": vidQuery[5], "tags": vidQuery[6],
                         "videoUploader": vidQuery[7], "commentsCount": vidQuery[8],
                         "videoViewCount": vidQuery[9],"ageLimit": vidQuery[10], "videoAverageRating": vidQuery[11],
                         "videoLikeCount": vidQuery[12], "videoDislikeCount": vidQuery[13], "videoDuration": vidQuery[14],
                         "channelId": chanQuery[0], "channelName": chanQuery[1],
                         "channelUrl": chanQuery[2],  "subscribersNumber": chanQuery[3], "channelTotalVideoViews": chanQuery[4],
                         "channelPublishedAt": chanQuery[5], "videosNumber": chanQuery[6]}
                return query
            else:
                print("No such data in the database.")

    def addData(self, dbData):
        # Checking if channel is in database. If it is, updating data
        if self.ifChannel(dbData.chanID):
            sql = "UPDATE `channels` t SET t.`subscriberCount` = %s, t.`viewsCount`= %s, t.`videosCount` = %s WHERE t.`channelID` like '" + dbData.chanID + "'"
            val = (dbData.chanSubscriberCount, dbData.chanViewCount, dbData.chanVideoCount)
            self.dbCursor.execute(sql, val)
            self.rdsdb.commit()
        else:
            # Adding new record to the channels Table if channel is not present in database
            sql = "INSERT INTO channels (channelID, channelName, channelUrl, subscriberCount, viewsCount, " \
                  "publishedAt, videosCount) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (dbData.chanID, dbData.chanName, dbData.chanWebUrl, dbData.chanSubscriberCount,
                      dbData.chanViewCount, dbData.chanPublishedAt, dbData.chanVideoCount)
            self.dbCursor.execute(sql, values)
            self.rdsdb.commit()
        # Checking if video is in database. If it is, updating data
        if self.ifVideo(dbData.vidID):
            sql = "UPDATE `videos` t SET t.`comments` = %s, t.`views`= %s,t.`rating` = %s, t.`like` = %s, " \
                  "t.`dislikes` = %s WHERE t.`videoID` like '" + dbData.vidID + "'"
            val = (
                dbData.vidCommentCount, dbData.vidViewCount, dbData.vidAverageRating, dbData.vidLikeCount,
                dbData.vidDislikeCount)
            self.dbCursor.execute(sql, val)
            self.rdsdb.commit()
        else:
            # Adding new record to the videos Table if video is not present in database
            sql = "INSERT INTO videos (videoID, channelID, videoTitle, videoUrl, thumbnailUrl, categories, " \
                  "tags, uploader, comments, views, ageLimit, rating, likes, dislikes, duration) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (dbData.vidID, dbData.chanID, dbData.vidTitle, dbData.vidWebUrl, dbData.vidThumbnail,
                      str(dbData.vidCategories)[1:][:-1], str(dbData.vidTags)[1:][:-1], dbData.vidUploader, dbData.vidCommentCount,
                      dbData.vidViewCount, dbData.vidAgeLimit, dbData.vidAverageRating, dbData.vidLikeCount,
                      dbData.vidDislikeCount, dbData.vidDuration)
            self.dbCursor.execute(sql, values)
            self.rdsdb.commit()

    def ifVideo(self, videoID):
        self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '" + videoID + "'")
        query = self.dbCursor.fetchone()
        print("ifVideo: " + str(query))
        if str(query) == "None":
            print("No such video in the database.")
            return False
        else:
            return True

    def ifChannel(self, chanID):
        self.dbCursor.execute("SELECT * FROM channels WHERE channelID like '" + chanID + "'")
        query = self.dbCursor.fetchone()
        print("ifChannel: " + str(query))
        if str(query) == "None":
            print("No such channel in the database.")
            return False
        return True
    #TODO Check if hist is present in database
    # def GetHist(self):

