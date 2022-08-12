from telegram import KeyboardButton, ReplyKeyboardMarkup
from sendmenu import *

def sendmenu(update, context):
    keyboard = [
        [
            KeyboardButton("📖 visit site"),
            KeyboardButton("🤖 use bot"),
            KeyboardButton("🤝 join group"),
            KeyboardButton("🧐 visit post"),

        ],
        [
            KeyboardButton("🔗 shorten link"),
            KeyboardButton("🙌 micro task"),
            KeyboardButton("🧩 captcha"),
            KeyboardButton("📹 watch video"),

        ],
        [
            KeyboardButton("💰 monitizegroup"),
            KeyboardButton("💸 monitizechannel"),
            KeyboardButton("😎 referral"),
            KeyboardButton("👛 wallet"),
        ],
        [
            KeyboardButton("🧳 myads"),
            KeyboardButton("⚙️ settings"),
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    welcome_txt = '''
🙏 welcome to faucetbank .

💰 earn trx from this bot daily 

🥇 it is the first 🎉 instant withdrawal bot

💸 you can get trx to faucetpay wallet automatically when you complete task

🏳️ earn from any location

🎁 earn trx from completing joinchat,messagingbot,visitpost etc.
    '''
    update.message.reply_text(welcome_txt, reply_markup=reply_markup)
