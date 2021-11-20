import mysql.connector

class MySQLVocabulary():
    def __init__(self):
        self.__connect_to_db()

    def __connect_to_db(self):
        self.conn = mysql.connector.connect(
        user="ardit700_student",
        password="ardit700_student",
        host="108.167.140.122",
        database="ardit700_pm1database"
        )

        self.cursor = self.conn.cursor()
        return self.conn, self.cursor

    def get_words(self):
        query = self.cursor.execute(f"SELECT Expression FROM Dictionary")
        results = self.cursor.fetchall()
        words = [x[0] for x in results]
        return words

    def get_definitions(self,word):
        query = self.cursor.execute(f"SELECT * FROM Dictionary WHERE Expression='{word}'")
        results = self.cursor.fetchall()
        if results:
            return [x[1] for x in results]
        else:
            return None


print(MySQLVocabulary().get_definitions('rain'))