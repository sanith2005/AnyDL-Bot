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

YTDL_REGEX = (r"^((?:https?:)?\/\/)"
              r"?((?:www|m)\.)"
              r"?((?:youtube\.com|youtu\.be|xvideos\.com|pornhub\.com"
              r"|xhamster\.com|xnxx\.com))"
              r"(\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)([\w\-]+)(\S+)?$")
s2tw = OpenCC('s2tw.json').convert


@Jebot.on_message(filters.command("help"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>My K-Drama Bot Help!
𝐼 𝓌𝒶𝓈 𝓂𝒶𝒹𝑒 𝒷𝓎 @sanithbimsara ღ</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "update", callback_data="update"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/Infinity_BOTs")
                                    ],[
                                      InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/AnyDL-Bot")
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
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/AnyDL-Bot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About AnyDL Bot!</b>

<b>♞ Developer:</b> <a href="https://t.me/ImJanindu">Janindu 🇱🇰</a>

<b>♞ Support:</b> <a href="https://t.me/InfinityBOTs_Support">Infinity BOTs Support</a>

<b>♞ Library:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>~ @Infinity_BOTs</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/AnyDL-Bot")
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

print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Jebot.run()
