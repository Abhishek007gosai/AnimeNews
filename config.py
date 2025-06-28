import os

API_ID = os.getenv("29245477")
API_HASH = os.getenv("0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = os.getenv("")
URL_A = os.getenv("URL_A")
URL_B = os.getenv("URL_B")
URL_C = os.getenv("URL_C")
START_PIC = os.getenv("https://litter.catbox.moe/m4c4wu.jpg")
MONGO_URI = os.getenv("mongodb+srv://BladexRobot:az50i6VCbZnez34y@cluster0.8uydmmp.mongodb.net/")
ADMINS = list(map(int, os.getenv("ADMINS", "7654385403").split()))
