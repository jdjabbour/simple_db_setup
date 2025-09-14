
import sqlite3
import unittest
from unittest.mock import patch, MagicMock

from src.connection_manager import ConnectionManager

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.db_name = ':memory:'
        self.conn = ConnectionManager(self.db_name).create_db_connection()

        self.cur = ConnectionManager(self.db_name).create_db_cursor(self.conn)

    def test_connection(self):
        self.assertIsNotNone(self.conn)

        self.assertIsInstance(self.cur, sqlite3.Cursor)

    def tearDown(self):
        """Close the database connection."""
        self.conn.close()

    # @patch('sqlite3.connect')
    # def test_user_password_success(self, mock_connection):
        
    #     cursor = mock_connection.return_value.cursor.return_value
    #     cursor.fetchall.side_effect = [[("val1","val2")]] 
        
    #     # function call
    #     resp = ConnectionManager().create_conn()
    #     self.assertEqual(resp, 1)