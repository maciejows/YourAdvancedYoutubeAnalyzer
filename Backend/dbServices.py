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
        query = Data()
        query.vidID = vidQuery[0]
        query.vidTitle = vidQuery[2]
        query.vidWebUrl = vidQuery[3]
        query.vidThumbnail = vidQuery[4]
        query.vidCategories = vidQuery[5]
        query.vidTags = vidQuery[6]
        query.vidUploader = vidQuery[7]
        query.vidCommentCount = vidQuery[8]
        query.vidViewCount = vidQuery[9]
        query.vidAgeLimit = vidQuery[10]
        query.vidAverageRating = vidQuery[15]
        query.vidLikeCount = vidQuery[16]
        query.vidDislikeCount = vidQuery[17]
        query.vidDuration = vidQuery[18]

        query.chanID = vidQuery[1]
        query.chanName = chanQuery[1]
        query.chanUrl = chanQuery[2]
        query.chanSubscriberCount = chanQuery[3]
        query.chanViewCount = chanQuery[4]
        query.chanPublishedAt = chanQuery[5]
        query.chanVideoCount = chanQuery[6]
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
#dupa.getChannelData("TESTchanID")
dupa.closeConnection()
