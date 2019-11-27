import mysql.connector
from mysql.connector import errorcode

class ytDB:
    def __init__(self):
        try:
            self.rdsdb = mysql.connector.connect(
                user="root",
                passwd="lubiemaslo",
                host="youtubeanalyzer.cqmx3x4uk8ob.us-east-1.rds.amazonaws.com",
                database="yayaDB"
            )
            print("succesfully connected to the database: " + str(self.rdsdb))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Acess denied/wrong  user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
            else:
                print(err)
        else: self.dbCursor = self.rdsdb.cursor()

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
      query = self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '"+ videoID +"'" )
      #print(query)
      return query

    def ifVideo(self, videoID):
      query = self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '" + videoID + "'")
      if query == "None": return False
      return True

    def addDataToDb(self, data):
      if ifVideo(video.videoID):
        self.dbCursor.execute("SELECT * FROM videos WHERE videoId like '" + videoID + "'")
      else:
        sql = "INSERT INTO videos (name, address) VALUES (%s, %s)"
        values()
        self.dbCursor.execute(sql, values)

dupa = ytDB()
print(dupa.getVideoData("yeeee"))
dupa.closeConnection()
