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


@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm @Muzix_robot.

I can download Audio from Youtube. Made by @sanithbimsara🇱🇰

Click "Help" button to find out more about how to use me.</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help👁️‍🗨️", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel🗣️", url="https://t.me/blackfoxprojects")
                                    ],[
                                      InlineKeyboardButton(
                                            "GitHub📟", url="https://github.com/sanith2005")
                                      InlineKeyboardButton(
                                            "Dev⌨️", url="https://github.com/sanith2005")
                                    ]]

                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>@Muzix_robot!

Just send a Youtube url to download it in .Mp3 format!

~ @Muzix_robot</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "GitHub", url="https://github.com/sanith2005")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About @Muzix_robot!</b>

<b>🏷 Developer:</b> <a href="https://t.me/sanithbimsara">Sanith Bimsara 🇱🇰</a>

<b>🏷️ Support:</b> <a href="https://t.me/blackfoxprojects">Black Fox Projects</a>

<b>🏷️ Whats App:</b> <a href="https://wa.me/qr/HJVDC27JHQJ3J1">Sanith</a>

<b>~ @Muzix_robot</b>""",
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


# https://docs.pyrogram.org/start/examples/bot_keyboards
# Reply with inline keyboard
@Jebot.on_message(filters.private
                   & filters.text
                   & ~filters.edited
                   & filters.regex(YTDL_REGEX))
async def ytdl_with_button(_, message: Message):
    await message.reply_text(
        "**Choose download Mp3🎶**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Audio 🎵",
                        callback_data="ytdl_audio"
                   ),
                ]
            ]
        ),
        quote=True
    )


@Jebot.on_callback_query(filters.regex("^ytdl_audio$"))
async def callback_query_ytdl_audio(_, callback_query):
    try:
        url = callback_query.message.reply_to_message.text
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': '%(title)s - %(extractor)s-%(id)s.%(ext)s',
            'writethumbnail': True
        }
        with YoutubeDL(ydl_opts) as ydl:
            message = callback_query.message
            await message.reply_chat_action("typing")
            info_dict = ydl.extract_info(url, download=False)
            # download
            await callback_query.edit_message_text("**Downloading audio...**")
            ydl.process_info(info_dict)
            # upload
            audio_file = ydl.prepare_filename(info_dict)
            task = asyncio.create_task(send_audio(message, info_dict,
                                                  audio_file))
            while not task.done():
                await asyncio.sleep(3)
                await message.reply_chat_action("upload_document")
            await message.reply_chat_action("cancel")
            await message.delete()
    except Exception as e:
        await message.reply_text(e)
    await callback_query.message.reply_to_message.delete()
    await callback_query.message.delete()


async def send_audio(message: Message, info_dict, audio_file):
    basename = audio_file.rsplit(".", 1)[-2]
    # .webm -> .weba
    if info_dict['ext'] == 'webm':
        audio_file_weba = basename + ".weba"
        os.rename(audio_file, audio_file_weba)
        audio_file = audio_file_weba
    # thumbnail
    thumbnail_url = info_dict['thumbnail']
    thumbnail_file = basename + "." + \
        get_file_extension_from_url(thumbnail_url)
    # info (s2tw)
    webpage_url = info_dict['webpage_url']
    title = '@muzix_robot - '+s2tw(info_dict['title'])
    caption = f"<b><a href=\"{webpage_url}\">{title}</a></b>"
    duration = int(float(info_dict['duration']))
    performer = s2tw(info_dict['uploader'])
    await message.reply_audio(audio_file, caption=caption, duration=duration,
                              performer=performer, title=title,
                              parse_mode='HTML', thumb=thumbnail_file)
    os.remove(audio_file)
    os.remove(thumbnail_file)

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
Join @muzix_robot
"""
)

Jebot.run()
