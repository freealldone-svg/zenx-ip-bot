from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import os
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")
BKASH = os.getenv("BKASH")
BINANCE = os.getenv("BINANCE")
SUPPORT = os.getenv("SUPPORT")

ADMIN_ID = 8069902198

USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def add_user(user_id):
    users = load_users()
    uid = str(user_id)

    if uid not in users:
        users[uid] = {
            "balance": 0,
            "history": []
        }
        save_users(users)
        
PROXIES = {
    "owl": ("🦉 Owl IP", 9),
    "abc": ("🔵 ABC IP", 255),
    "rocket": ("🚀 Rocket IP", 160),
    "rapid": ("⚡ Rapid IP", 127),
    "datamplus": ("🌐 Datamplus", 150),
}
