import sys

sys.path.append("./dbfolder")
sys.path.append("./payment")

from faucetpay import faucetpay
from mysqlfunc import mysqldb
from telegram import Bot

from pay import payuser

a = mysqldb()
b = faucetpay()

print(b.checkuser("kmano2915@gmail.com"))