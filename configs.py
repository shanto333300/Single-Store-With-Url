import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "22971260"))
  API_HASH = os.environ.get("API_HASH", "39b93b45f525642b9c732f43185e4ab0")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "BdFileShareBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001619644038"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "gyanilinks.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "64054f98b2ae99ecbfcd0841352611d841952f0b")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1150044195"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dramagdrive07:tyfcNDI59dA4AtoX@cluster0.rot1t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002277197696"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [KING](https://telegram.me/KING_SOUROB)
 
 I am Super noob Please Support My Hard Work.

[Update Channel](https://t.me/Ks_Bots)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
