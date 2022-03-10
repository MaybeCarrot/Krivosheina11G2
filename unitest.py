import sqlite3
import unittest

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

class DataBase:
    def __init__(self, path: str):
        self.__connection = sqlite3.connect(path)
        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__connection.close()

    def goods(self, id: int):
        request = 'SELECT(SELECT name FROM types WHERE id = type_id ) AS type_name,(SELECT name FROM goods WHERE id = :good_id) AS good_name,price FROM price'
        return self.__cursor.execute(request, {'good_id': id}).fetchall()

    def userBorn(self, id: int):
        request = 'SELECT name, sername, (SELECT name FROM goods WHERE id = streams.good_id) AS good_name, date  FROM client WHERE born >= "2003/01/01" '
        return self.__cursor.execute(request, {'born': id}).fetchall()
    

    def type(self, id: int):
        request = 'SELECT name, kol FROM goods WHERE type_id = (SELECT id FROM types WHERE name = :type_name) '
        return self.__cursor.execute(request, {'type_name': id}).fetchall()
    
    def priceDates(self, id: int):
        request = 'SELECT(SELECT name FROM goods WHERE id = streams.good_id) AS good_name, price FROM price WHERE date >= :dates;'
        return self.__cursor.execute(request, {'dates': id}).fetchall()

    @property
    def get_cursor(self):
        return self.__cursor

    @property
    def conn(self):
        return self.__connection
    

def task():
    cursor.execute('SELECT DISTINCT(born) FROM client')

conn.close()

class Test(unittest.TestCase):
    
    def test_goods(self):
        for i in range(1, 4 + 1):
            request = self.__temp.goods(id=i)
            self.assertEqual(1, len(request))

    def test_userBorn(self):
        for i in range(1, 3 + 1):
            request = self.__temp.userBorn(id=i)
            self.assertEqual(1, len(request))

    def test_type(self):
        for i in range(1, 3 + 1):
            request = self.__temp.type(id=i)
            self.assertEqual(1, len(request))

    def test_priceDates(self):
        for i in range(1, 3 + 1):
            request = self.__temp.priceDates(id=i)
            self.assertEqual(1, len(request))

    def tearDown(self):
        self.__temp.conn.close()
        
    def Set(self):
        self.__temp = DataBase(':memory:')
        self.__temp.get_cursor.executescript(
            '''
            CREATE TABLE IF NOT EXISTS "Client"(
                "id" INTEGER UNIQUE,
                "name" TEXT NOT NULL,
                "surname" TEXT NOT NULL,
                "date" DATE NOT NULL DEFAULT'2000-00-00',
                "born" DATE NOT NULL DEFAULT'666-06-06',
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            
            CREATE TABLE IF NOT EXISTS "Types"(
                "id" INTEGER UNIQUE NOT NULL,
                "name" TEXT NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            
            CREATE TABLE IF NOT EXISTS "Goods"(
                "id" INTEGER UNIQUE,
                "type_id" INTEGER NOT NULL,
                "name" TEXT NOT NULL,
                "kol" INTEGER,
                FOREIGN KEY("type_id") REFERENCES "Types"("id"),
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            
            CREATE TABLE IF NOT EXISTS "Operation"(
                "id" INTEGER UNIQUE,
                "good_id" INTEGER NOT NULL,
                "type_id" INTEGER NOT NULL,
                "client_id" INTEGER NOT NULL,
                "kol" INTEGER NOT NULL,
                "order_date" DATE NOT NULL DEFAULT'2000-00-00',
                "delivery_date" DATE NOT NULL DEFAULT'6666-00-00',
                FOREIGN KEY("client_id") REFERENCES "Client"("id"),
                FOREIGN KEY("type_id") REFERENCES "Types"("id"),
                FOREIGN KEY("good_id") REFERENCES "Goods"("id"),
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            
            CREATE TABLE IF NOT EXISTS "Price"(
                "good_id" INTEGER NOT NULL,
                "price" INTEGER NOT NULL,
                "date" DATE NOT NULL DEFAULT'2000-00-00',
                FOREIGN KEY("good_id") REFERENCES "Goods"("id")
            );
            
            '''
        )

if __name__ == '__main__':
    unittest.main(failfast=False)