#Don't remove This Line From Here. @Teamxo77| @Teamxo77
#Github :- TeamPiyush | sidra
from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
BOT_NAME = os.environ.get("BOT_NAME")
START_IMG1 = os.environ.get("START_IMG1")
START_IMG2 = os.environ.get("START_IMG2", None)
START_IMG3 = os.environ.get("START_IMG3", None)
START_IMG4 = os.environ.get("START_IMG4", None)
START_IMG5 = os.environ.get("START_IMG5", None)
START_IMG6 = os.environ.get("START_IMG6", None)
START_IMG7 = os.environ.get("START_IMG7", None)
START_IMG8 = os.environ.get("START_IMG8", None)
START_IMG9 = os.environ.get("START_IMG9", None)
START_IMG10 = os.environ.get("START_IMG10", None)
STKR = os.environ.get("STKR")
STKR1 = os.environ.get("STKR1", None)
STKR2 = os.environ.get("STKR2", None)
STKR3 = os.environ.get("STKR3", None)
STKR4 = os.environ.get("STKR4", None)
STKR5 = os.environ.get("STKR5", None)
STKR6 = os.environ.get("STKR6", None)
STKR7 = os.environ.get("STKR7", None)
STKR8 = os.environ.get("STKR8", None)
STKR9 = os.environ.get("STKR9", None)

bot = Client(
    "Sidra" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


PHOTO = [
    START_IMG1,
    START_IMG2,
    START_IMG3,
    START_IMG4,
    START_IMG5,
    START_IMG6,
    START_IMG7,
    START_IMG8,
    START_IMG9,
    START_IMG10,
]

EMOJIOS = [ 
      "👻",
      "❣️",
      "💋",
      "👅",
      "⚡",
      "🤡",
      "👄",
      "🎃",
      "🎩",
      "🕊",
]
      
STICKER = [
      STKR,
      STKR1,
      STKR2,
      STKR3,
      STKR4,
      STKR5,
      STKR6,
      STKR7,
      STKR8,
      STKR9,
]
START = f"""
**๏ Hey, I AM [{Sidra}]({START_IMG})**
**๏ I'M SIDRA CHAT BOT **
**๏ I WANT CHST YIU BABY 🙈..**
**➻ 𝐀𝐧 𝐀𝐈-𝐁𝐚𝐬𝐞𝐝 𝐂𝐡𝐚𝐭𝐛𝐨𝐭.**
**──────────────────**
**➻ 𝐔𝐬𝐚𝐠𝐞 /chatbot [on/off]**
**๏ 𝐓𝐨 𝐆𝐞𝐭 𝐇𝐄𝐋𝐏 𝐔𝐬𝐞 /help**
"""
PIYUSH_OP = [
    [
        InlineKeyboardButton(text="💓Sidra Baby💓", url=f"https://t.me/Muskan_Queen"),
        InlineKeyboardButton(text="💫Robin chat 💫", url=f"https://t.me/Teamxo77"),
    ],
    [
        InlineKeyboardButton(
            text="🥺 MUJE ADD KR LO NA YAAL 🥺",
            url=f"https://t.me/Sidra_robot?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🥰 Help & Commands  Baby 🥰", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🤑 Source code 🤑", callback_data="SOURCE"),
        InlineKeyboardButton(text="😜 𝐀𝐛𝐨𝐮𝐭 😜", callback_data="ABOUT"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="🥺 𝐀𝐝𝐝 𝐌𝐞 𝐁𝐚𝐛𝐲 🥺",
             url=f"https://t.me/Sidra_robot?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="💬 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💬", 
                              url=f"https://t.me/Teamxo77",
         ),
     ],
]
HELP_READ = f"**𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐟𝐨𝐫 [𝐒𝐢𝐝𝐫𝐚](https://t.me/Sidra_robot)**\n**──────────────────**\n**➻ 𝐔𝐬𝐞** `/chatbot on` **𝐓𝐨 𝐄𝐧𝐚𝐛𝐥𝐞 𝐂𝐡𝐚𝐭𝐁𝐨𝐭.**\n**➻ 𝐔𝐬𝐞** `/chatbot off` **𝐓𝐨 𝐃𝐢𝐬𝐚𝐛𝐥𝐞 𝐭𝐡𝐞 𝐂𝐡𝐚𝐭𝐁𝐨𝐭.**\n**๏ 𝐍𝐨𝐭𝐞 ➻ 𝐁𝐨𝐭𝐡 𝐭𝐡𝐞 𝐀𝐛𝐨𝐯𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐟𝐨𝐫 𝐂𝐡𝐚𝐭-𝐁𝐨𝐭 𝐨𝐧/ᴏғғ 𝐖𝐨𝐫𝐤 𝐢𝐧 𝐆𝐫𝐨𝐮𝐩 𝐎𝐧𝐥𝐲!!**\n**──────────────────**\n**➻ 𝐔𝐬𝐞** `/ping` **𝐓𝐨 𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐏𝐢𝐧𝐠 𝐨𝐟 𝐭𝐡𝐞 𝐁𝐨𝐭.**\n**➻ 𝐔𝐬𝐞** `/repo` **𝐅𝐨𝐫 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞.**\n**──────────────────**\n**©️ @Teamxo77**"
BACK = [
     [
           InlineKeyboardButton(text="◀️ 𝐁𝐀𝐂𝐊 ◀️", callback_data="BACK"),
     ],
]
ABOUT_BTN = [
      [
           InlineKeyboardButton(text="❤️ 𝐆𝐫𝐨𝐮𝐩 ❤️", url=f"https://t.me/Teamxo77"),  
           InlineKeyboardButton(text="😍 𝐇𝐞𝐥𝐩 😍", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="💌 𝗖𝗥𝗘𝗔𝗧𝗢𝗥 💌", url=f"https://t.me/OpSangram"), 
           InlineKeyboardButton(text="🤑 𝐒𝐨𝐮𝐫𝐜𝐞 🤑", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="🔄 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🔄", url=f"https://t.me/Babyi_loveyou"),  
           InlineKeyboardButton(text="◀️ 𝐁𝐀𝐂𝐊 ◀️", callback_data="BACK"),
      ],
]
SOURCE_READ = f"**𝐇𝐞𝐲👋, 𝐓𝐡𝐞 𝐂𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐨𝐟 [Queen](https://t.me/Sidra_robot) 𝐈𝐬 𝐆𝐢𝐯𝐞𝐧 𝐁𝐞𝐥𝐨𝐰.**\n**𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐨𝐫𝐤 𝐭𝐡𝐞 𝐑𝐞𝐩𝐨 & 𝐆𝐢𝐯𝐞 𝐭𝐡𝐞 𝐒𝐭𝐚𝐫 ✯**\n**──────────────────**\n**𝐇𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 [𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞](https://github.com/WCFteam/Smart-Chatbot)**\n**──────────────────**\n**𝐈𝐟 𝐲𝐨𝐮 𝐟𝐚𝐜𝐞 𝐚𝐧𝐲 𝐩𝐫𝐨𝐛𝐥𝐞𝐦 𝐭𝐡𝐞𝐧 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐚𝐭 [𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩](https://t.me/Teamxo77).**"

ABOUT_READ = f"""
**➻ [𝐒𝐢𝐝𝐫𝐚](https://t.me/Sidra_robot) 𝐈𝐬 𝐚𝐧 𝐀𝐢 𝐁𝐚𝐬𝐞𝐝 𝐂𝐡𝐚𝐭-𝐁𝐨𝐭.**
**➻ [𝐒𝐢𝐝𝐫𝐚](https://t.me/Sidra_robot) 𝐑𝐞𝐩𝐥𝐢𝐞𝐬 𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲 𝐭𝐨 𝐚 𝐔𝐬𝐞𝐫.**
**➻ 𝐇𝐞𝐥𝐩 𝐘𝐨𝐮 𝐢𝐧 𝐌𝐚𝐤𝐞𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐜𝐭𝐢𝐯𝐞.**
**➻ 𝐅𝐢𝐫𝐬𝐭 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐨𝐭 𝐁𝐚𝐬𝐞𝐝 𝐨𝐧 𝐏𝐲𝐭𝐡𝐨𝐧 𝐰𝐢𝐭𝐡 𝐌𝐨𝐧𝐠𝐨-𝐃𝐛 𝐚𝐬 𝐚 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞**
**➻ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 [Sangram](https://t.me/OpSangram) 𝐚𝐧𝐝 [𝐖𝐂𝐅](https://t.me/Teamxo77) **
**──────────────────**
**➻ 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 𝐭𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐆𝐢𝐯𝐞𝐧 𝐁𝐞𝐥𝐨𝐰 𝐟𝐨𝐫 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐁𝐚𝐬𝐢𝐜 𝐇𝐞𝐥𝐩 𝐚𝐧𝐝 𝐈𝐧𝐟𝐨 𝐀𝐛𝐨𝐮𝐭 [𝐒𝐢𝐝𝐫𝐚](https://t.me/Sidra_robot)**
"""
@bot.on_message(filters.command(["start", "aistart", f"start@Sidra_robot"]))
async def restart(client, m: Message):
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(1.5)
    await accha.edit("__•́  ‿ ,•̀ 🩸 Mai aa rhi hu baby 💋🥺.__")
    await asyncio.sleep(0.3)
    await accha.edit("__(っ◔◡◔)っ ♥ wait kro na baby 🥺 ♥.....__")
    await asyncio.sleep(0.3)
    await accha.edit("__(っ◔◡◔)っ ♥ mai aagyi baby 💋 ♥..__")
    await asyncio.sleep(0.3)
    await accha.delete()
    umm = await m.reply_sticker(
              sticker = random.choice(STICKER),
    )
    await asyncio.sleep(3)
    await umm.delete()
    await m.reply_photo(
        photo = random.choice(PHOTO),
        caption=f"""**๏ 𝐇𝐞𝐲, 𝐈 𝐚𝐦 [𝐒𝐢𝐝𝐫𝐚](t.me/Sidra_robot)**\n**๏ 𝐈"𝐦 𝐒𝐢𝐝𝐫𝐚 𝐨𝐫 𝐚 𝐂𝐡𝐚𝐭𝐛𝐨𝐭.**\n**๏ 𝐈 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐜𝐡𝐚𝐭 𝐰𝐢𝐭𝐡 𝐲𝐨𝐮 𝐛𝐚𝐛𝐲 🥺.**\n**➻ 𝐀𝐧 𝐀𝐢-𝐁𝐚𝐬𝐞𝐝 𝐂𝐡𝐚𝐭𝐁𝐨𝐭.**\n**──────────────────**\n**➻ 𝐔𝐬𝐚𝐠𝐞 /chatbot [on/off]**\n**๏ 𝐓𝐨 𝐆𝐞𝐭 𝐇𝐞𝐥𝐩 𝐮𝐬𝐞 /help**""",
        reply_markup=InlineKeyboardMarkup(PIYUSH_OP),
    )
@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(BACK),
                      disable_web_page_preview=True,
     )
    elif query.data == "BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(PIYUSH_OP),
     )
    elif query.data == "SOURCE":
            await query.message.edit(
                   text = SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,

     )
    elif query.data == "ABOUT":
            await query.message.edit(
                    text = ABOUT_READ,
                    reply_markup = InlineKeyboardMarkup(ABOUT_BTN),
                    disable_web_page_preview=True,
     )
@bot.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(
                   text= SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,
      )
@bot.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_text(
                        text = HELP_READ,
                        reply_markup= InlineKeyboardMarkup(BACK),
       )

@bot.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "__ριɳɠιɳɠ...__"
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("__𝐏𝐢𝐧𝐠𝐢𝐧𝐠.....__")
        await asyncio.sleep(0.25)
        await txxt.edit_text("__𝐏𝐢𝐧𝐠𝐢𝐧𝐠...__")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=random.choice(PHOTO),
                             caption=f"𝐇𝐞𝐲 𝐁𝐚𝐛𝐲!!\n**[𝐒𝐢𝐝𝐫𝐚](t.me/Sidra_robot)** Is Alive 🥀 and Working fine with a ping ᴏꜰ\n➥ `{ms}` ms\n\n**𝐌𝐚𝐝𝐞 𝐛𝐲 [Muskan](https://t.me/Muskan_Queen)**",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

@bot.on_message(
    filters.command(["chatbot off", f"chatbot@{BOT_USERNAME} off"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    emiliadb = MongoClient(MONGO_URL)    
    emilia = emiliadb["EmiliaDb"]["Queen"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "You are not admin"
            )
    is_emilia = emilia.find_one({"chat_id": message.chat.id})
    if not is_emilia:
        emilia.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Disabled!")
    if is_emilia:
        await message.reply_text(f"ChatBot Already Disabled")
    

@bot.on_message(
    filters.command(["chatbot on", f"chatbot@{BOT_USERNAME} on"] ,prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    emiliadb = MongoClient(MONGO_URL)    
    emilia = emiliadb["EmiliaDb"]["Queen"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_emilia = emilia.find_one({"chat_id": message.chat.id})
    if not is_emilia:           
        await message.reply_text(f"Chatbot Already Enabled")
    if is_emilia:
        emilia.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Enabled!")
    

@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**𝐔𝐬𝐚𝐠𝐞:**\n/**chatbot [on/off]**\n**𝐂𝐡𝐚𝐭-𝐁𝐨𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝(s) 𝐖𝐨𝐫𝐤𝐬 𝐢𝐧 𝐆𝐫𝐨𝐮𝐩 𝐎𝐧𝐥𝐲!**")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def emiliaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       emiliadb = MongoClient(MONGO_URL)
       emilia = emiliadb["EmiliaDb"]["Queen"] 
       is_emilia = emilia.find_one({"chat_id": message.chat.id})
       if not is_emilia:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       emiliadb = MongoClient(MONGO_URL)
       emilia = emiliadb["EmiliaDb"]["Queen"] 
       is_emilia = emilia.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_emilia:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def emiliastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       emiliadb = MongoClient(MONGO_URL)
       emilia = emiliadb["EmiliaDb"]["Queen"] 
       is_emilia = emilia.find_one({"chat_id": message.chat.id})
       if not is_emilia:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       emiliadb = MongoClient(MONGO_URL)
       emilia = emiliadb["EmiliaDb"]["Queen"] 
       is_emilia = emilia.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_emilia:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def emiliaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def emiliaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"{BOT_NAME} ɪs ᴀʟɪᴠᴇ!")      
bot.run()
