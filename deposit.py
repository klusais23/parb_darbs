

class Deposit:

    def __init__(self, deposit=0 , term=0 , rate=0):
        self.deposit = deposit
        self.term = term
        self.rate = rate


    def interest(self):
        self.oldDeposit = self.deposit

        for i in range(self.term):
            self.deposit = self.deposit + self.deposit * self.rate


        self.result = self.deposit - self.oldDeposit

        return self.result

#
# a = Deposit(deposit=1000 , term=3 , rate= 0.05)
# b = a.interest()
# print(b)