from mysqlfunc import mysqldb
from tiny import tiny
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, KeyboardButton
import sys
sys.path.append("./dbfolder")



def check_and_set_wallet(update):
    if not mysqldb().is_set_wallet(update.message.from_user.id):
        update.message.reply_text("whenever you complete a task , you get paid instantly using faucetpay")
        keyboard = [[
            InlineKeyboardButton(
                "SIGNUP", url='https://faucetpay.io/?r=3538990')
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "if you don't have faucet pay wallet.\nclick here to sign up faucet pay ", reply_markup=reply_markup)
        update.message.reply_text(
            " 👉 send your faucetpay email to set automatic withdrawal")
        tiny.set_user(update.message.from_user.id, "setfaucetpay")
        return True
    return False
