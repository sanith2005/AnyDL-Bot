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
                                            "User Guid 📃", url="https://telegra.ph/My-K-Drama-Bot-User-Guid-04-18"),
                                        InlineKeyboardButton(
                                            "Rate Us ⭐️", url="https://t.me/tlgrmcbot?start=mykdrama_bot-review"),
                                    ],[
                                      InlineKeyboardButton(
                                            "Creator 😊 ", url="https://t.me/sanithbimsara"),
                                   ],[
                                        InlineKeyboardButton(
                                            "Request 👨‍💻", url="https://t.me/sanithbimsara"),
                                        InlineKeyboardButton(
                                            "Feedback 🌀", url="https://t.me/sanithbimsara"),
                                   ],[
                                      InlineKeyboardButton(
                                            "Other ProJects 💾 ", url="https://t.me/mykdramabot/763"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("update"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>My K-Drama Bot Was Successfully Updated ✅</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back 🔙", callback_data="help"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("More"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>More Optations👨‍🔧</b>""",
           
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Feedback 🌀", url="https://t.me/sanithbimsara"),
                                        InlineKeyboardButton(
                                            "Creator 😊 ", url="https://t.me/sanithbimsara"),
                                    ],[
                                      InlineKeyboardButton(
                                            "Other ProJects 💾 ", url="https://t.me/mykdramabot/763"),
                                   ],[
                                        InlineKeyboardButton(
                                            "Back 🔙", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Main Menu 🔝", callback_data="start"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Jebot.run()
