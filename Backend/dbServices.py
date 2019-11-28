import os

import mysql.connector
from mysql.connector import errorcode
from data.py import data


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

    def getVideoData(self, videoID):
        query = self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '" + videoID + "'")
        # print(query)
        return query

    def getChannelData(self, channelID):
        query = self.dbCursor.execute("SELECT * FROM channels WHERE videoId like '" + channelID + "'")

    def getData(self, data):
        self.getVideoData(data.vidID)
        self.getChannel(data.chanID)

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
print(dupa.getVideoData("yeeee"))
dupa.closeConnection()
