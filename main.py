from sendmenu import *
import logging

from telegram import Bot,InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, KeyboardButton, user
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
from func import *
from middleware import *
import sys
sys.path.append("./dbfolder")
sys.path.append("./payment")

from pay import payuser
from faucetpay import faucetpay
from mysqlfunc import mysqldb
from tiny import tiny
from extrafunc import completebot, completechat, editAd, txt






faucetwallet = faucetpay()


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)







def start(update: Update, context: CallbackContext) -> None:
    sendmenu(update, context)
    tiny.set_user(update.message.from_user.id, "start")
    if not mysqldb().isexist_user(update.message.from_user.id):
        if context.args:
            mysqldb().insert_user(update.message.from_user.id, "0", context.args[0])
        else:
            mysqldb().insert_user(update.message.from_user.id, "0", 2039990859)
    check_and_set_wallet(update)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    print(update.callback_query.from_user.id)

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="please wait...")

    txt(update, context, query)
    completebot(update, context, query)
    completechat(update,context,query)
    editAd(update, context)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def text(update: Update, context: CallbackContext) -> None:
    if update.message.text == "🔙 back":
        start(update, context)

    if update.message.text == "❌ cancel":
        tiny.set_user(update.message.from_user.id, "start")
        sendmenu(update, context)
    

    if tiny.get_user_state(update.message.from_user.id).startswith("changeadtitle_"):
        mysqldb().update_ad_title(str(tiny.get_user_state(update.message.from_user.id)).split("changeadtitle_")[1],update.message.text)
        update.message.reply_text("title of ad is updated!")
        tiny.set_user(update.message.from_user.id,"start")
        myads(update,context)
        return
    if tiny.get_user_state(update.message.from_user.id).startswith("changeaddesc_"):
        mysqldb().update_ad_desc(str(tiny.get_user_state(update.message.from_user.id)).split("changeaddesc_")[1],update.message.text)
        update.message.reply_text("description of ad is updated!")
        tiny.set_user(update.message.from_user.id,"start")
        myads(update,context)

    if tiny.get_user_state(update.message.from_user.id).startswith("changeadcpc_"):
        try:
            i=float(update.message.text)
            if i > 0.0049 and i<10.1:
                mysqldb().update_ad_cpc(str(tiny.get_user_state(update.message.from_user.id)).split("changeadcpc_")[1],i)
                update.message.reply_text("cpc of ad is updated!")
                tiny.set_user(update.message.from_user.id,"start")
                myads(update,context)
            else:
                update.message.reply_text("CPC should be between 0.005 and 10")
        except:
            update.message.reply_text("CPC should be between 0.005 and 10")
        
    
    if str(tiny.get_user_state(update.message.from_user.id)).startswith("admessagebot_"):
        promotebot=str(tiny.get_user_state(update.message.from_user.id)).split("admessagebot_")[1]
        #examble bot's url = https://t.me/botusername
        if update.message.text.startswith("https://t.me/"+promotebot):
            mysqldb().createad("messagebot",update.message.from_user.id,promotebot,update.message.text)
            update.message.reply_text("when you add the budget to the bot , the ad will activated automatically . so before adding the budget to the ad , edit the ad's info")
            tiny.set_user(update.message.from_user.id,"start")
            myads(update,context)
        else:
            update.message.reply_text("send correct url of @"+promotebot )


    if tiny.get_user_state(update.message.from_user.id) == "changefaucetpay":
        if faucetwallet.checkuser(update.message.text):
            mysqldb().update_user_walletaddress(
                update.message.from_user.id, update.message.text)
            tiny.set_user(update.message.from_user.id, "start")
            update.message.reply_text(
                "wallet address is changed successfully!")
            sendmenu(update, context)
        else:
            update.message.reply_text("❌ wrong faucetpay wallet email address")
            change_wallet(update, context)
        return True

    if tiny.get_user_state(update.message.from_user.id) == "setfaucetpay":
        if faucetwallet.checkuser(update.message.text):
            mysqldb().update_user_walletaddress(
                update.message.from_user.id, update.message.text)
            tiny.set_user(update.message.from_user.id, "start")
            update.message.reply_text(
                "wallet address is added to do automatic withdrawal . complete your first task and earn some amount of trx")
            sendmenu(update, context)
        else:
            update.message.reply_text("❌ wrong faucetpay wallet email address")
        return True

    if tiny.get_user_state(update.message.from_user.id)=="createad":
        if update.message.text=="🤖 use bot":
            tiny.set_user(update.message.from_user.id,"ad_bot")
            update.message.reply_text("forward a message from the bot")
        elif update.message.text=="🤝 join group":
            tiny.set_user(update.message.from_user.id,"ad_joinchat")
            update.message.reply_text("make me an admin of the group and forward a message from the channel or group")
        return



    # update.message.reply_text(update.message.text)
    if update.message.text == "📖 visit site":
        visit_site(update, context)
    if update.message.text == "🤖 use bot":
        use_bot(update, context)
    if update.message.text == "🤝 join group":
        join_group(update, context)
    if update.message.text == "🧐 visit post":
        visit_post(update, context)
    if update.message.text == "🔗 shorten link":
        shorten_link(update, context)
    if update.message.text == "🙌 micro task":
        micro_task(update, context)
    if update.message.text == "🧩 captcha":
        captcha(update, context)
    if update.message.text == "📹 watch video":
        watch_video(update, context)
    if update.message.text == "💸 monitizechannel":
        monetize_channel(update, context)
    if update.message.text == "😎 referral":
        referral(update, context)
    if update.message.text == "👛 wallet":
        wallet(update, context)
    if update.message.text == "🧳 myads":
        myads(update, context)
    if update.message.text == "⚙️ settings":
        settings(update, context)

     # sub menu of myads
    if update.message.text == "➕ create ad":
        createad(update, context)


    # sub menu of wallet
    if update.message.text == "🔁 change wallet":
        change_wallet(update, context)

def checkforward(update: Update,context: CallbackContext):
    userstate=tiny.get_user_state(update.message.from_user.id)

    if str(userstate)=="ad_bot":
        print(update.message.forward_from)
        promotechat=update.message.forward_from['username']
        update.message.reply_text("send the bot's url")
        tiny.set_user(update.message.from_user.id,"admessagebot_"+promotechat)
    
    if str(userstate)=="ad_joinchat":
        promotechat=update.message.forward_from['username']
        if bot.get_chat_member("@"+promotechat,bot.get_me()['id'])['status']=="administrator":
            mysqldb().createad("joinchat",update.message.from_user.id,promotechat)
            update.message.reply_text("when you add budget to the ad , the ad will be activated automatically . update the ad info")
            tiny.set_user(update.message.from_user.id,"start")
            myads(update,context)
        else:
            update.message.reply_text("make me a admin of your chat and then send the username of your chat")





    if str(userstate).startswith("messagebot_"):
        get_messagebot_campaign_id=str(userstate).split("_")[1]
        if update.message.forward_from['username']==mysqldb().campaignid_to_info(get_messagebot_campaign_id)[4]:
            if not mysqldb().is_completed_already(update.message.from_user.id,get_messagebot_campaign_id):
                payment_status=payuser.sendreward(get_messagebot_campaign_id,update.message.from_user.id)
                if payment_status==True:
                    update.message.reply_text("your reward is claimed ! \ncheck user faucetpay balance \ni added "+str(float(mysqldb().campaignid_to_info(get_messagebot_campaign_id)[5])/2)+"trx")
                else:
                    if faucetwallet.checkuser(mysqldb().get_user_Wallet(update.message.from_user.id)):
                        update.message.reply_text("the task is not avilable!")
                    else:
                        update.message.reply_text("go to balance and update your faucetpay email")
                tiny.set_user(update.message.from_user.id,"start")
            else:
                update.message.reply_text("you completed the task already!")
                sendmenu(update,context)
                tiny.set_user(update.message.from_user.id,"start")
        else:
            update.message.reply_text("your forward message is from wrong chat")

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    token = "5345982495:AAFT-hrbLkRuYLuhnpLcSrMOI8-wgt0CkLc"
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.text & ~ Filters.command & ~Filters.forwarded, text))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.text & ~ Filters.command & Filters.forwarded, checkforward))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
