#from fibs import *

import unitest

import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def task():
    cursor.execute('SELECT DISTINCT(born) FROM client')

conn.close()

class Test(unitest.TestCase):
    
    def test_task(self):
        self.assertEqual(task(), '12/12/1212', 'Should be 12/12/1212' )