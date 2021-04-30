class Atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber        

    def CashWithdrawl(self):
        print("Cash Withdrawed")

    def CheckBalance(self):
        print("Balance Checked")