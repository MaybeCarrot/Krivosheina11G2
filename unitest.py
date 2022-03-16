import sqlite3
import unittest

print('test')

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

class DataBase:
    def __init__(self, path: str):
        self.__connection = sqlite3.connect(path)
        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__connection.close()

    def user(self, id: int):
        request = 'SELECT name, surname, date, born FROM Client WHERE client_id = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()
    
    def type(self, id: int):
        request = 'SELECT name FROM Types WHERE type_id = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()    
    
    def goods(self, id: int):
        request = 'SELECT type_id, name, kol FROM Goods WHERE good_id = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()

    def price(self, id: int):
        request = 'SELECT price, date FROM Price WHERE good_id = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()

    @property
    def get_cursor(self):
        return self.__cursor

    @property
    def conn(self):
        return self.__connection



class Test(unittest.TestCase):
            
    def test_type(self):
        print("tekst3")
        for i in range(1, 2 + 1):
            request = self.__temp.type(id=i)
            self.assertEqual(1, len(request))

    def test_user(self):
        print("tekst2")
        for i in range(1, 2 + 1):
            request = self.__temp.user(id=i)
            self.assertEqual(1, len(request))


    def test_goods(self):
        print("tekst")
        for i in range(1, 4 + 1):
            request = self.__temp.goods(id=i)
            self.assertEqual(1, len(request))
            
    def test_price(self):
        print("tekst4")
        for i in range(1, 3 + 1):
            request = self.__temp.price(id=i)
            self.assertEqual(1, len(request))    


    def tearDown(self):
        self.__temp.conn.close()
        
    def setUp(self):
        self.__temp = DataBase(':memory:')
        self.__temp.get_cursor.executescript(
            '''
            CREATE TABLE IF NOT EXISTS "Client"(
                "client_id" INTEGER UNIQUE,
                "name" TEXT NOT NULL,
                "surname" TEXT NOT NULL,
                "date" DATE NOT NULL DEFAULT'2000-00-00',
                "born" DATE NOT NULL DEFAULT'666-06-06',
                PRIMARY KEY("client_id" AUTOINCREMENT)
            );
            
            INSERT INTO Client VALUES(1, 'A', 'C', '2222-22-22', '1111-11-11');
            INSERT INTO Client VALUES(2, 'B', 'D', '2222-22-22', '1111-11-11');
            
            CREATE TABLE IF NOT EXISTS "Types"(
                "type_id" INTEGER UNIQUE NOT NULL,
                "name" TEXT NOT NULL,
                PRIMARY KEY("type_id" AUTOINCREMENT)
            );
            
            INSERT INTO Types VALUES(1, 'A');
            INSERT INTO Types VALUES(2, 'B');
            
            CREATE TABLE IF NOT EXISTS "Goods"(
                "good_id" INTEGER UNIQUE,
                "type_id" INTEGER NOT NULL,
                "name" TEXT NOT NULL,
                "kol" INTEGER,
                FOREIGN KEY("type_id") REFERENCES "Types"("type_id"),
                PRIMARY KEY("good_id" AUTOINCREMENT)
            );
            
            INSERT INTO Goods VALUES(1, 1, 'A', 14);
            INSERT INTO Goods VALUES(2, 1, 'B', 14);
            INSERT INTO Goods VALUES(3, 2, 'A', 14);
            INSERT INTO Goods VALUES(4, 2, 'B', 14);
            
            CREATE TABLE IF NOT EXISTS "Price"(
                "good_id" INTEGER NOT NULL,
                "price" INTEGER NOT NULL,
                "date" DATE NOT NULL DEFAULT'2000-00-00',
                FOREIGN KEY("good_id") REFERENCES "Goods"("good_id")
            );
            
            INSERT INTO Price VALUES(1, 12, '1111-11-11');
            INSERT INTO Price VALUES(2, 300, '1111-11-11');
            INSERT INTO Price VALUES(3, 790, '1111-11-11');
            
            '''
        )

if __name__ == '__main__':
    unittest.main(failfast=False)