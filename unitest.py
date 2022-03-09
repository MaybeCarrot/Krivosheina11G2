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

class Test(unitest.TestCase):
    
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
        
if __name__ == '__main__':  # точка входа в программу
    unittest.main(failfast=False)