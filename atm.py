class Atm(object):
    def __init__(self,atm_card_number,pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
    def cash_withdrawal(self):
        print("Cash Withdrawal")
    def balance_enquiry(self):
        print("Balance Enquiry")
    def cash_deposit(self):
        print("Cash deposit")
bank_atm = Atm(12345678,"XXXX")
print(bank_atm.cash_withdrawal())