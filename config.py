import os

API_HASH = os.getenv("API_HASH")
API_HASH = os.environ("API_HASH")
BOT_TOKEN = os.environ("BOT_TOKEN")
#URL_A = os.getenv("URL_A")
#URL_B = os.getenv("URL_B")
#URL_C = os.getenv("URL_C")
START_PIC = os.getenv("https://litter.catbox.moe/m4c4wu.jpg")
MONGO_URI = os.getenv("")
ADMINS = list(map(int, os.getenv("ADMINS", "7654385403").split()))
