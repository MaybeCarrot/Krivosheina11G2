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

    def goods(self, id2: int):
        request = f'SELECT(SELECT name FROM types WHERE id = {id2} ) AS type_name,(SELECT name FROM goods WHERE id = {id2}) AS good_name,price FROM price'
        return self.__cursor.execute(request).fetchall()

    def userBorn(self, id1: int):
        request = f'SELECT name, surname, (SELECT name FROM goods WHERE id = {id1}) AS good_name, date  FROM client WHERE born >= 2003-01-01 '
        return self.__cursor.execute(request).fetchall()
    

    def type(self, id3: int):
        request = f'SELECT name, kol FROM goods WHERE type_id = {id3} '
        return self.__cursor.execute(request).fetchall()
    
    def priceDates(self, id4: int):
        request = f'SELECT(SELECT name FROM goods WHERE id = {id4}) AS good_name, price FROM price WHERE date >= 1111-11-11 '
        return self.__cursor.execute(request).fetchall()

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
        print("tekst")
        for i in range(1, 4 + 1):
            request = self.__temp.goods(id2=i)
            print(request)

            self.assertEqual(1, len(request))
            

    def test_userBorn(self):
        print("tekst2")
        for i in range(1, 3 + 1):
            request = self.__temp.userBorn(id1=i)
            self.assertEqual(1, len(request))

    def test_type(self):
        print("tekst3")
        for i in range(1, 3 + 1):
            request = self.__temp.type(id3=i)
            self.assertEqual(1, len(request))

    def test_priceDates(self):
        print("tekst4")
        for i in range(1, 3 + 1):
            request = self.__temp.priceDates(id4=i)
            self.assertEqual(1, len(request))

    def tearDown(self):
        self.__temp.conn.close()
        
    def setUp(self):
        self.__temp = DataBase('1.db')
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
            
            INSERT INTO Client VALUES(1, 'A', 'A', '2222-22-22', '1111-11-11');
            INSERT INTO Client VALUES(2, 'B', 'B', '2222-22-22', '1111-11-11');
            
            CREATE TABLE IF NOT EXISTS "Types"(
                "id" INTEGER UNIQUE NOT NULL,
                "name" TEXT NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            
            INSERT INTO Types VALUES(1, 'A');
            INSERT INTO Types VALUES(1, 'B');
            
            CREATE TABLE IF NOT EXISTS "Goods"(
                "id" INTEGER UNIQUE,
                "type_id" INTEGER NOT NULL,
                "name" TEXT NOT NULL,
                "kol" INTEGER,
                FOREIGN KEY("type_id") REFERENCES "Types"("id"),
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            
            INSERT INTO Goods VALUES(1, 1, 'A', 14);
            INSERT INTO Goods VALUES(2, 1, 'B', 14);
            INSERT INTO Goods VALUES(3, 2, 'A', 14);
            INSERT INTO Goods VALUES(4, 2, 'B', 14);
            
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
            
            INSERT INTO Operation VALUES(1, 1, 1, 1, 2, '1122-11-22', '2211-22-11');
            
            CREATE TABLE IF NOT EXISTS "Price"(
                "good_id" INTEGER NOT NULL,
                "price" INTEGER NOT NULL,
                "date" DATE NOT NULL DEFAULT'2000-00-00',
                FOREIGN KEY("good_id") REFERENCES "Goods"("id")
            );
            
            INSERT INTO Prise VALUES(1, 12, '1111-11-11');
            INSERT INTO Prise VALUES(2, 300, '1111-11-11');
            INSERT INTO Prise VALUES(4, 790, '1111-11-11');
            
            '''
        )

if __name__ == '__main__':
    unittest.main(failfast=False)