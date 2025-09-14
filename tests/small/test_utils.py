
import unittest

from src.utils.build_schema import BuildSchema



class UtilsTestCase(unittest.TestCase):

    def test_build_schema(self):
        test_schema = {
            'table': 'test',
            'columns': ['test1', 'test2']
        }
        test_res = BuildSchema(test_schema).build_proxy_values()
        self.assertEqual(test_res, '(?,?)')

 

    
