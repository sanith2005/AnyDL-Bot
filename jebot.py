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
               text="""<b>Hey There, I'M <a href="https://telegra.ph/file/71917d2fb9e17e5cbfd9e.jpg">My K-Drama Bot</a>

I can download any Koren Tv Series. Made by @sanithbimsara🇱🇰

Hit How to Use button to find out more about how to use me</b>""",   
                            
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>My K-Drama Bot Help!</b>
<b>More Information,
Please Click<\b> <a href="https://telegra.ph/My-K-Drama-Bot-Help-03-31">Help</a><b>👈<\b>


~ @blackfoxprojects</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/blackfoxprojects")
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

<b>♞ Developer:</b> <a href="https://t.me/sanitjbimsara">Sanith</a>

<b>♞ Support:</b> <a href="https://t.me/blackfoxprojects">Black Fox Projects</a>

<b>♞ Server:</b> <a href="https://heroku.com">Heroku</a>

<b>~ @blackfoxprojects</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Restart Bot", callback_data="Start"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")


@Jebot.on_message(filters.command("update"))
async def updated (client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>My K-Drama Bot Was Successfully Updated✅</b>""",   
                            
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
        await start(bot, update.message)

print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Jebot.run()
