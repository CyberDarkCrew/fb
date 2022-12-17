from info import *
import os

try:
    import whois
    import folium
    import geocoder
    import smtplib
    import sys
    import time
    import threading as thr
except:


bot = telebot.TeleBot(token_bot)

def replys(m):
    msg = m.text.split(" ")
    msg2 = m.text.split(",")
    match msg[0]:
        case "/whois":
            try:
                w = whois.whois(msg[1])
                whoisw = str(w)
                bot.reply_to(m, whoisw)

            except Exception:
                bot.reply_to(m, "⚠ Please Enter Any Site")
                bot.reply_to(m, "✅ Example \"/whois example.com\"")

        case "/cmd":
            bot.reply_to(m,"Commands \n1️⃣ /whois\n2️⃣ /sms \n3️⃣ /ip_info")
        case "/start":
            bot.reply_to(m, "Coded By Mr.Dark @L_N_X_0 \n\nClick On /cmd")
        case "/sms":
            bot.reply_to(m, "⚠ This has been stopped by admin")
        case "/ip_info":
            our_ip = geocoder.ip(msg[1])
            location = our_ip.latlng
            x = str(location)
            location1 = x.replace("[", "")
            location2 = location1.replace("]", "")
            locationx = "https://www.google.com/maps/place/"+location2

            bot.reply_to(m,locationx)
        case "/help":
            bot.reply_to(m,"")