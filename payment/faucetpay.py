from FaucetPy import Api
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class faucetpay:
    def __init__(self) -> None:
        self.wallet = Api("11ea9bb844c00d9af95b6ff20a8d52db36cf0e80")

    def check(self, email):
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False

    def checkuser(self, email):
        if self.check(email):
            #print(self.wallet.checkAddress(address=email))
            return self.wallet.checkAddress(address=email)['message'] == "OK"
        else:
            return False

    def send_trx_to_user(self, email, amount):
        return self.wallet.sendTo(to=email, amount=amount, currency="trx")

    def checkbalance(self):
        return self.wallet.get_balance(currency="trx")
