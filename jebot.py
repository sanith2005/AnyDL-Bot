import os
import asyncio
from urllib.parse import urlparse
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_dl import YoutubeDL
from opencc import OpenCC
from config import Config

Jebot = Client(
   "YT Downloader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)


@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<code>Hey There, I'm My K-Drama Bot

I can download Korean TV series. Made by @sanithbimsara 🇱🇰

Hit help button to find out more about how to use me</code>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Update🔄", callback_data="update"),
                                         InlineKeyboardButton(
                                            "Help❓", callback_data="help"),
                                    ],[
                                      InlineKeyboardButton(
                                            "Channel🗣", url="https://t.me/blackfoxprojects"),
                                    ],[
                                   InlineKeyboardButton(
                                            "Request📩", url="http://t.me/r_e_q_u_e_s_t_bot"),
                                         InlineKeyboardButton(
                                            "More🛠", callback_data="more"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>My K-Drama Bot Help!</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help❓", url="https://telegra.ph/My-K-Drama-Bot-Help-04-01"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "More🛠", callback_data="more"),
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About My K-Drama Bot!</b>

<b>💎 Developer:</b> <a href="https://t.me/sanithbimsara">Sanith 🇱🇰</a>

<b>💎 Support:</b> <a href="https://t.me/blackfoxprojects">Black Fox Projects</a>

<b>💎 Server:</b> <a href="https://heroku.com">Heroku</a>

<b>💎 Request:</b> <a href="http://t.me/r_e_q_u_e_s_t_bot">Request Dramas</a>

<b>💎 User Guide:</b> <a href="https://telegra.ph/My-K-Drama-Bot-Help-04-01">How to Use My K-Drama Bot</a>

<b>💎 Language:</b> <a href="https://www.python.org/">Python</a>


<b>~ @blackfoxprojects</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
      
@Jebot.on_message(filters.command("update"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>My K-Drama Bot Was successfully Updated!✅</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
      
@Jebot.on_message(filters.command("more"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>More🛠</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Rate⭐️⭐️", url="https://t.me/tlgrmcbot?start=mykdrama_bot-review"),
                                         InlineKeyboardButton(
                                            "Feedback🌀", url="http://t.me/r_e_q_u_e_s_t_bot"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Updates And notifications", url="https://telegra.ph/My-K-Drama-Bot-Update--Notification-04-01"),
                                        InlineKeyboardButton(
                                            "Dev", url="https://t.me/sanithbimsara"),
                                ],[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
      
@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)
      elif "update" in cb_data:
        await update.message.delete()
        await update(bot, update.message)
       elif "more" in cb_data:
        await update.message.delete()
        await more(bot, update.message)
         
print(
    """
Bot Started!
Join @blackfoxprojects
"""
)

Jebot.run()
