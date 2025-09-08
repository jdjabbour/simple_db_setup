

class Calcs:
    def __init__(self, price, cost):
        self.price = float(price)
        self.cost = float(cost)

    def gross_profit(self):
        try:
            res = round(((1-self.cost/self.price) * 100), 2)
            return res
        except ZeroDivisionError as e:
            res = '0.00'
            return res
        
    def highlight_gross_profit(self, gp):
        if gp < 30.00:
            gp = f":red[{gp}]"
            return gp
        if gp > 30.00 and gp < 50:
            gp = f":yellow[{gp}]"
            return gp
        else:
            gp = f":green[{gp}]"
            return gp


        
    