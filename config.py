import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29271987"))
API_HASH = getenv("7f64fefc37d03b7281060321d4ed5035")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","DarkGamer7t2rl")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","infinity_powerfull_bot")
# --------------------------------------------------------
BOT_NAME = getenv("darkxmusic")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", 1002843572899))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7487670897))


## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/itzarjuna1/knight-king",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dark_x_knight_musiczz_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/dark_knight_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION","BQG-p7MAcJuyxPrlPmdKrPBn49Ryl-vHSN0gXy5sKr5sWEY87b5H2b4lnALJgumAzcMLmKgS40wAPrHdk8pwalTzirVQBNgQCfpaY-5W5Aj8-nL7IvKgXW_RlgXVpEtn_2iCaqGf6cJW2HoDc-n1ofDLCu7katiGnKzo37WWa9MDjT4QSiLaoTkXrruQbKbQdlh2DUx3dbpgKhL0NP4TeEA8b4GiWq8Y7ZOKikYZhiVtjzqRUKiSAWAqFI1X3ZfRv9k55tkgB2mwTJrfXgrVTDgAWRKuluvAitpb6Mpii1PxrzDAf90T7dQgW1Md9fWV5Tr5Wh1mfxOJknOPiokUfIKcm_fdrwAAAAHbA4EyAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/urwe8v.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/urwe8v.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"
STATS_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/urwe8v.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/urwe8v.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/urwe8v.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
