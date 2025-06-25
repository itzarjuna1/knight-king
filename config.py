import os
import re
from pyrogram import filters

# Heroku automatically provides these from Config Vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Optional bot settings
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "DEADCALAM")
BOT_USERNAME = os.getenv("BOT_USERNAME", "Anya_lip_bot")
BOT_NAME = os.getenv("BOT_NAME", "AnyaXMusic")

# MongoDB URI from cloud.mongodb.com
MONGO_DB_URI = os.getenv(
    "MONGO_DB_URI",
    "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Duration limit (in minutes)
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 17000))
DURATION_LIMIT = int(
    sum(int(x) * 60**i for i, x in enumerate(reversed(f"{DURATION_LIMIT_MIN}:00".split(":"))))
)

# Logging group/channel
LOGGER_ID = int(os.getenv("LOGGER_ID", -1002556228441))

# Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", 7495324168))

# Heroku-related vars
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# Git repo
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/Gxinfinity/ANYA_MUSIC")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# Support URLs
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/gxinfinity_support")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/infinitygx_bot_support")

if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("❌ Invalid SUPPORT_CHANNEL URL. It must start with http/https.")
if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("❌ Invalid SUPPORT_CHAT URL. It must start with http/https.")

# Optional settings
AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# YouTube/Spotify/Apple playlist fetch limit
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# File size limits (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))  # 100MB
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))  # 1GB

# String Sessions from @StringFatherBot
STRING1 = os.getenv("STRING_SESSION")
STRING2 = os.getenv("STRING_SESSION2")
STRING3 = os.getenv("STRING_SESSION3")
STRING4 = os.getenv("STRING_SESSION4")
STRING5 = os.getenv("STRING_SESSION5")

# Bot filters and other memory
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/rca1m3.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/9cevdg.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/i493lf.jpg"
STATS_IMG_URL = "https://files.catbox.moe/i0qmgf.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"