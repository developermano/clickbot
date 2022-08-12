from turtle import up
from faucetpay import faucetpay
from shortenlinkdb import linkdb
from func import join_group, shorten_link, use_bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
import requests
import json
import string
import random
import time
import sys
from tiny import tiny
from telegram import Bot
from sendmenu import *



sys.path.append("./dbfolder")
sys.path.append("./payment")
from pay import payuser
from mysqlfunc import mysqldb
token = "2028867157:AAGLQujsMJc1K_hTIpjkhlYzkmBdPRgaNds"
bot=Bot(token)

wallet=faucetpay()


def checkdelay(program, chatid):
    try:
        d = time.time() - float(linkdb.get(program + "_" + str(chatid)))
        return d > 3600
    except:
        return "error"


def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def setdelay(program, chatid):
    linkdb.set(program + "_" + str(chatid), time.time())


def txt(update: Update, context: CallbackContext, query) -> None:
    program = query.data
    programs = [
        "linksly", "shrinkme", "clicksfly", "shrinkearn", "ouo", "clksh",
        "shortzon", "shrink", "uii", "oke"
    ]
    api_url = [
        "https://linksly.co/api?api=02d3d29b17e81ff788f778dff5404a235aebcb46&url="
        + "faucetbank.xyz/claim.php?id=",
        "https://shrinkme.io/api?api=c19e858f604c99b835d70d01ad10f615e7149b12&url="
        + "faucetbank.xyz/claim.php?id=",
        "https://clicksfly.com/api?api=e18e6a50b9336328f77ccd40aa1f1e31040bd389&url="
        + "faucetbank.xyz/claim.php?id=",
        "https://shrinkearn.com/api?api=6fd1f6722e1556fbc27dd3a907f8fa81257d3fcf&url="
        + "faucetbank.xyz/claim.php?id=",
        "http://ouo.io/api/grKNePKA?s=" +
        "faucetbank.xyz/claim.php?id=",
        "https://clk.sh/api?api=07bb8368a396a339019e69c45de2ef3db75b4eac&url="
        + "faucetbank.xyz/claim.php?id=",
        "https://shortzon.com/api?api=011b8056011239a47dd5c0505a749765dd85e779&url="
        + "faucetbank.xyz/claim.php?id=",
        "https://shrink.pe/api?api=2cb9e12596197b7d5f9d269e9fadf27274f42fb4&url="
        + "faucetbank.xyz/claim.php?id=",
        "https://uii.io/api?api=0b4b9981aab91b780d59008f4f0555be51402183&url="
        + "faucetbank.xyz/claim.php?id=",
        "https://oke.io/api/?api=627180d0d32d1919ba5e0da2084e5d72933fba6f&url="
        + "faucetbank.xyz/claim.php?id="
    ]
    if program in programs:
        if checkdelay(program, update.callback_query.from_user.id) == "error":
            linkdb.set(program + "_" +
                       str(update.callback_query.from_user.id), 1653792341)
        if checkdelay(program, update.callback_query.from_user.id):
            randtxt = id_generator()
            x = requests.get(api_url[programs.index(program)] +
                             randtxt)
            linkdb.set(str(randtxt), update.callback_query.from_user.id)
            exprogram = ["ouo"]
            if program in exprogram:
                if program == "ouo":
                    keyboard = [[
                        InlineKeyboardButton("OPEN LINK", url=x.text)
                    ]]

                    reply_markup = InlineKeyboardMarkup(keyboard)
                    query.edit_message_text(
                        "1. open the link \n2.if you go final page , you will get trx instantly to your faucetpay wallet .\n3. get the trx instantly   ",
                        reply_markup=reply_markup)
            else:
                y = json.loads(x.text)
                keyboard = [[
                    InlineKeyboardButton("OPEN LINK", url=y['shortenedUrl'])
                ]]


                reply_markup = InlineKeyboardMarkup(keyboard)
                query.edit_message_text(
                    "1. open the link \n2.if you go final page , you will get bitcoin instantly to your faucetpay wallet .\n3. get the bitcoin instantly   ",
                    reply_markup=reply_markup)
            setdelay(program, update.callback_query.from_user.id)
        else:
            query.edit_message_text(
                str(3600 -
                    round(time.time() -
                          float(linkdb.get(program + "_" + str(update.callback_query.from_user.id))))) +
                " seconds are left to get next link from this shortenlink provider . so please try another shortlink provider from this bot")



def completebot(update : Update, context, query):
    if str(query.data).startswith("messagebot_"):
        get_messagebot_campaign_id=str(query.data).split("_")[1]
        if not mysqldb().is_completed_already(update.callback_query.from_user.id,get_messagebot_campaign_id):
            update.callback_query.delete_message()
            keyboard = [
        [
            KeyboardButton("🔙 back"),
         ]
         ]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            campaigninfo=mysqldb().campaignid_to_info(get_messagebot_campaign_id)
            bot.send_message(update.callback_query.from_user.id,text="⤵️forward a message from the required chat @"+campaigninfo[4]+" to claim reward ",reply_markup=reply_markup)
            tiny.set_user(update.callback_query.from_user.id,"messagebot_"+get_messagebot_campaign_id)
        else:
            query.edit_message_text(text="😭 sorry , you completed the job already ")


def completechat(update:Update,context,query):
    if str(query.data).startswith("joinchat_"):
        get_messagebot_campaign_id=str(query.data).split("_")[1]
        if not mysqldb().is_completed_already(update.callback_query.from_user.id,get_messagebot_campaign_id):
            if True:
                member=bot.get_chat_member("@"+mysqldb().campaignid_to_info(get_messagebot_campaign_id)[4],update.callback_query.from_user.id)
                if member['status']=="member":
                    print('s')
                    payment_status=payuser.sendreward(get_messagebot_campaign_id,update.callback_query.from_user.id)
                    if payment_status==True:
                        print('s')
                        update.callback_query.edit_message_text("your reward is claimed ! \ncheck user faucetpay balance \ni added "+str(float(mysqldb().campaignid_to_info(get_messagebot_campaign_id)[5])/2)+"trx")
                    else:
                        if wallet.checkuser(mysqldb().get_user_Wallet(update.callback_query.from_user.id)):
                            update.callback_query.edit_message_text("the task is not avilable!")
                        else:
                            update.callback_query.edit_message_text("go to balance and update your faucetpay email")
                    
                else:
                    update.callback_query.edit_message_text("your are not at the group")
                print("joinchat")
        else:
            query.edit_message_text(text="😭 sorry , you completed the job already!")
            tiny.set_user(update.callback_query.from_user.id,"start")



def editAd(update:Update,context:CallbackContext)->None:
    txt=update.callback_query.data
    if txt.startswith("changeadtitle_"):
        tiny.set_user(update.callback_query.from_user.id,txt)
        keyboard = [
        [KeyboardButton("❌ cancel"),
         ]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        bot.send_message(update.callback_query.from_user.id,"send title of ad ",reply_markup=reply_markup)
        update.callback_query.delete_message()
    if txt.startswith("changeaddesc_"):
        tiny.set_user(update.callback_query.from_user.id,txt)
        keyboard = [
        [KeyboardButton("❌ cancel"),
         ]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        bot.send_message(update.callback_query.from_user.id,"send description of ad ",reply_markup=reply_markup)
        update.callback_query.delete_message()
    if txt.startswith("changeadcpc_"):
        tiny.set_user(update.callback_query.from_user.id,txt)
        keyboard = [
        [KeyboardButton("❌ cancel"),
         ]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        bot.send_message(update.callback_query.from_user.id,"send cpc",reply_markup=reply_markup)
        update.callback_query.delete_message()

