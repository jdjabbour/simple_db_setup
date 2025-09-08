
import unittest

try:
    from src.calc_manager import Calcs
    # from src.view_main import highlight_gross_profit
except:
    from calc_manager import Calcs
    # from view_main import highlight_gross_profit



class MainTestCase(unittest.TestCase):

    def test_gross_profit_clean(self):
        price = '13.99'
        cost = '10.00'
        test_res = Calcs(price, cost).gross_profit()
        self.assertEqual(test_res, 28.52)

    def test_gross_profit_zero(self):
        price = float('0.00')
        cost = float('0.00')
        test_res = Calcs(price, cost).gross_profit()
        self.assertEqual(test_res, '0.00')

    def test_gross_profit_yellow(self):
        price = float('10.00')
        cost = float('6.00')
        gp = Calcs(price, cost).gross_profit()
        gp_yw_test = Calcs(price, cost).highlight_gross_profit(gp)
        self.assertEqual(gp_yw_test, f":yellow[{gp}]")

    
