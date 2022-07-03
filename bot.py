import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>𝙷𝙴𝙻𝙻𝙾 {},\n𝙸'𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝙱𝙾𝚃 𝚃𝙾 𝙳𝙴𝙻𝙴𝚃𝙴 𝙶𝚁𝙾𝚄𝙿 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙰𝙵𝚃𝙴𝚁 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝚃𝙸𝙼𝙴. 𝙱𝚄𝚃 𝚈𝙾𝚄 𝙲𝙰𝙽𝙽𝙾𝚃 𝚄𝚂𝙴 𝙼𝙴. 𝙸 𝙰𝙼 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝚆𝙸𝚃𝙷 <a href=https://t.me/shamil_shaz_1>🅢︎🅗︎🅐︎🅜︎🅘︎🅛︎</a></b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention)),
        disable_web_page_preview=True      
        
    )

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
