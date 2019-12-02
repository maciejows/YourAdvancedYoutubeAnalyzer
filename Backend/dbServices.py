import os

import mysql.connector
from mysql.connector import errorcode
from data import Data


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
        vidQuery = self.getVideoData(vidID)
        chanQuery = self.getChannelData(vidQuery[1])
        print(vidQuery + chanQuery)

        query = {"videoTitle": vidQuery[2], "thumbnailURL": vidQuery[4], "videoId": vidQuery[0],
                 "videoUrl": vidQuery[3], "tags": vidQuery[6],
                 "videoUploader": vidQuery[7], "videoCategories": vidQuery[5],
                 "ageLimit": vidQuery[10], "videoViewCount": vidQuery[9],
                 "videoDislikeCount": vidQuery[17], "commentsCount": vidQuery[8],
                 "videoLikeCount": vidQuery[16], "videoAverageRating": vidQuery[15],
                 "videoDuration": vidQuery[18], "channelId": vidQuery[1], "channelName": chanQuery[1],
                 "channelUrl": chanQuery[2], "channelTotalVideoViews": chanQuery[4],
                 "subscribersNumber": chanQuery[3], "videosNumber": chanQuery[6],
                 "channelPublishedAt": chanQuery[5]}
        return query

    def addData(self, data):
        if self.ifVideo(data.vidID):
            self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '" + data.vidID + "'")
        else:
            sql = "INSERT INTO videos (name, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (data.vidID, data.vidUploader, data.vidWebUrl)
            self.dbCursor.execute(sql, values)

    def ifVideo(self, videoID):
        query = self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '" + videoID + "'")
        if query == "None": return False
        return True


dupa = ytDB()
dupa.getVideoData("TESTvidID")
dupa.getData("TESTvidID")
# dupa.getChannelData("TESTchanID")
dupa.closeConnection()
