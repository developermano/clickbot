from telegram import Bot,InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, KeyboardButton,User
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
from telegram import ParseMode
import sys
sys.path.append("./dbfolder")
sys.path.append("./payment")
from tiny import tiny
from mysqlfunc import mysqldb
token = "2028867157:AAGLQujsMJc1K_hTIpjkhlYzkmBdPRgaNds"
bot=Bot(token)




def visit_site(update: Update, context):
    update.message.reply_text("there is  no ads .")
    return
    txt='''
<b>{}</b>
<i>{}</i>

--------------------

1. click visit button
2. visit the site
3. claim your reward with clicking visited button
    '''
    result=mysqldb().list_ad_to_user(update.message.from_user.id,'visitad')
    if result==None:
        update.message.reply_text("there is no ads")
    else:
        txt1=txt.format(result[1],result[2])
        keyboard=[[
            InlineKeyboardButton("👀 visit site", url=result[4]),
            InlineKeyboardButton("🚩 report", callback_data="report_"+str(result[0]))
        ]

    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(txt1,parse_mode=ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)




def use_bot(update, context):
    txt='''
<b>{}</b>
<i>{}</i>

--------------------

1. click message bot button
2. send message to the bot
3. claim your reward with clicking complete button
    '''
    result=mysqldb().list_ad_to_user(update.message.from_user.id,'messagebot')
    if result==None:
        update.message.reply_text("there is no ads")
    else:
        txt1=txt.format(result[1],result[2])
        keyboard=[[
            InlineKeyboardButton("💬 message bot", url=str(result[8]))],[
            InlineKeyboardButton("✅ complete", callback_data="messagebot_"+str(result[0])),
            InlineKeyboardButton("🚩 report", callback_data="report_"+str(result[0]))]
        

    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(txt1,parse_mode=ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)



def join_group(update, context):
    txt='''
<b>{}</b>
<i>{}</i>

--------------------

1. click join button
2. join the group or channel 
3. claim your reward with clicking joined button
    '''
    result=mysqldb().list_ad_to_user(update.message.from_user.id,'joinchat')
    if result==None:
        update.message.reply_text("there is no ads")
    else:
        txt1=txt.format(result[1],result[2])
        keyboard=[[
            InlineKeyboardButton("💬 join chat", url="https://t.me/"+result[4])],[
            InlineKeyboardButton("✅ complete", callback_data="joinchat_"+str(result[0])),
            InlineKeyboardButton("🚩 report", callback_data="report_"+str(result[0]))]
        

    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(txt1,parse_mode=ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)


def visit_post(update : Update, context):
    result=mysqldb().list_ad_to_user(update.message.from_user.id,'visitpost')
    if result==None:
        update.message.reply_text("there is no ads")
    else:
        msg='''
        1. just watch post
        2. after 10seconds , you can claim your reward .
        3. click complete button to claim reward
        '''
        keyboard=[[
            
            InlineKeyboardButton("✅ complete", callback_data="visitpost_"+str(result[0])),
            InlineKeyboardButton("🚩 report", callback_data="report_"+str(result[0]))]
        

    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.forward_message(chat_id=update.message.from_user.id,from_chat_id=result[4],message_id=result[8])
        update.message.reply_text(msg,parse_mode=ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)



def shorten_link(update, context):
    keyboard = [

        [
            InlineKeyboardButton("ouo", callback_data="ouo"),
            InlineKeyboardButton("shrinkme", callback_data="shrinkme"),


        ],
        [
            InlineKeyboardButton("clicksfly", callback_data="clicksfly"),
            InlineKeyboardButton("linksly", callback_data="linksly"),
        ],
        [
            InlineKeyboardButton("clksh", callback_data="clksh"),
            InlineKeyboardButton("shortzon", callback_data="shortzon"),

        ],
        [
            InlineKeyboardButton("oke", callback_data="oke"),
            InlineKeyboardButton("uii", callback_data="uii"),

        ],
        [
            InlineKeyboardButton("shrinkearn", callback_data="shrinkearn"),
            InlineKeyboardButton("shrink", callback_data="shrink")
        ]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    shorten_link_message = '''
🔗🔗 earn from shorten link 🔗🔗


🥇 click shorten link provider
🥈 click shorten link
🥉 if you go final page of the shorten link , you will get bitcoin automatically 
   
    '''
    update.message.reply_text(shorten_link_message, reply_markup=reply_markup)


def micro_task(update, context):
    update.message.reply_text("there is no ads.")


def captcha(update, context):
    update.message.reply_text("there is no ads.")


def watch_video(update, context):
    update.message.reply_text("there is no ads.")





def monetize_channel(update, context):
    update.message.reply_text("coming soon")


def referral(update, context):
    referral_txt = '''

earn from your referral :

10% of your referral task earnings ⚔

💰 earn extra income using this referral program and refer your friends using this link:

👉 https://t.me/Faucet_click_bot?start='''+str(update.message.from_user.id)
    update.message.reply_text(referral_txt)


def wallet(update, context):
    keyboard = [[
        KeyboardButton("🔁 change wallet"),
    ],
        [KeyboardButton("🔙 back"),
         ]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def myads(update: Update, context):
    if len(mysqldb().list_my_ads(update.message.from_user.id)) !=0:
        keyboard = [[ 
            KeyboardButton("➕ create ad"),
        ],
            [KeyboardButton("🔙 back"),
            ]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text('you have '+str(len(mysqldb().list_my_ads(update.message.from_user.id)))+'ads', reply_markup=reply_markup)
        for i in mysqldb().list_my_ads(update.message.from_user.id):
            txt_ad='''
<b>adtitle: {}</b>
<i>ad description : {}</i>
-------------------------
<i>cpc : {}</i>
<i>totalbudget : {}</i>
<i>adtype : {}</i>
<i>adurl : {}</i>
            '''
            txt_ad1=txt_ad.format(i[1],i[2],i[5],i[6],i[3],i[4])
            keyboard = [
                [
                        InlineKeyboardButton("edit title", callback_data=str("changeadtitle_")+str(i[0])),
                        InlineKeyboardButton("edit description", callback_data=str("changeaddesc_")+str(i[0]))
                ],
                    [
                        InlineKeyboardButton("change cpc", callback_data=str("changeadcpc_")+str(i[0])),
                    ],
                    [
                        InlineKeyboardButton("add budget", url=str("http://13.127.155.81/clickbot/deposit.php?id="+str(i[0])))
                    ],
                    
                    ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(txt_ad1,parse_mode=ParseMode.HTML,disable_web_page_preview=True,reply_markup=reply_markup)
    else:
        keyboard = [[ 
            KeyboardButton("➕ create ad"),
        ],
            [KeyboardButton("🔙 back"),
            ]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text('you have no ads', reply_markup=reply_markup)


def settings(update, context):
    settings_txt = '''
    it is under construction
    '''
    update.message.reply_text(settings_txt)


# submenu of ads
def createad(update:Update, context):
    tiny.set_user(update.message.from_user.id,"createad")
    keyboard = [[
        KeyboardButton("🤖 use bot"),
        KeyboardButton("🤝 join group")
    ],
        [KeyboardButton("❌ cancel"),
         ]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text('Please choose your ad type:', reply_markup=reply_markup)

# submenu of wallet


def change_wallet(update: Update, context: CallbackContext):
    tiny.set_user(update.message.from_user.id, "changefaucetpay")
    keyboard = [
        [
            KeyboardButton("❌ cancel"),
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        " 👉 send your faucetpay email to change automatic withdrawal email", reply_markup=reply_markup)
