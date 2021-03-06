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

START_MSG = "<b>π·π΄π»π»πΎ {},\nπΈ'πΌ π° ππΈπΌπΏπ»π΄ π±πΎπ ππΎ π³π΄π»π΄ππ΄ πΆππΎππΏ πΌπ΄πππ°πΆπ΄π π°π΅ππ΄π π° ππΏπ΄π²πΈπ΅πΈπ² ππΈπΌπ΄. π±ππ ππΎπ π²π°π½π½πΎπ πππ΄ πΌπ΄. πΈ π°πΌ ππΎππΊπΈπ½πΆ ππΈππ· <a href=https://t.me/shamil_shaz_1>π’οΈποΈποΈποΈποΈποΈ</a></b>"


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
    await message.reply(START_MSG.format(message.from_user.mention))
        
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
