import sys
import time
import telepot
import requests
from telepot.loop import MessageLoop
import json
import datetime
import os


import htmlParser as hp
import secrets


magazine_url = "http://jurnali-online.ru/xaker"
ydiskURL = "https://cloud-api.yandex.net/v1/disk/public/resources?public_key="
tmpFile = "tmp"
scriptDir = os.path.dirname(__file__)
abs_file_path = os.path.join(scriptDir, tmpFile)

bot = telepot.Bot(secrets.TOKEN)

lastFromWeb = hp.getLast(magazine_url)
lastSended = hp.read(abs_file_path)
if lastSended != lastFromWeb:
    (title, urlImage, urlDisk) = hp.getItemInfo(lastFromWeb)
    bot.sendMessage(secrets.chatID, "New Release!!!")
    bot.sendMessage(secrets.chatID, title + "\n" + urlDisk)
    hp.save(lastFromWeb, abs_file_path)