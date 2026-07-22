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

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def add_user(user_id):
    users = load_users()
    user_id = str(user_id)

    if user_id not in users:
        users[user_id] = {
            "balance": 0
        }
        save_users(users)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_user(update.effective_user.id)

    keyboard = [
        [
            InlineKeyboardButton("💰 My Balance", callback_data="balance"),
            InlineKeyboardButton("🛒 Buy Proxy", callback_data="buy"),
        ],
        [
            InlineKeyboardButton("💳 Deposit", callback_data="deposit"),
            InlineKeyboardButton("📞 Support", callback_data="support"),
        ],
        [
            InlineKeyboardButton("🌐 Language", callback_data="language"),
            InlineKeyboardButton("🛡 MB Checker", callback_data="checker"),
        ],
    ]

    await update.message.reply_text(
        "👋 Welcome to ZENX IP BOT",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
  
 PROXIES = {
    "owl": ("🦉 Owl IP", "৳9/IP"),
    "abc": ("🔵 ABC IP", "৳255/IP"),
    "rocket": ("🚀 Rocket IP", "৳160/IP"),
    "rapid": ("⚡ Rapid IP", "৳127/IP"),
    "datamplus": ("🌐 Datamplus", "৳150/IP"),
}


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    users = load_users()
    user_id = str(query.from_user.id)

    if query.data == "balance":
        balance = users.get(user_id, {}).get("balance", 0)
        await query.message.reply_text(
            f"💰 Your Balance: ৳{balance}"
        )

    elif query.data == "buy":
        keyboard = []

        for key, value in PROXIES.items():
            keyboard.append([
                InlineKeyboardButton(
                    f"{value[0]} - {value[1]}",
                    callback_data=key
                )
            ])

        await query.message.reply_text(
            "🛒 Choose Your Proxy",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data in PROXIES:
        proxy = PROXIES[query.data]

        await query.message.reply_text(
            f"📦 {proxy[0]}\n\n"
            f"💵 Price: {proxy[1]}\n\n"
            f"📩 Contact Support:\n{SUPPORT}"
        )

    elif query.data == "deposit":
        await query.message.reply_text(
            f"💳 Deposit Methods\n\n"
            f"📱 bKash: {BKASH}\n"
            f"🟡 Binance UID: {BINANCE}\n\n"
            f"Payment করার পরে TxID Support-এ পাঠান।"
        )

    elif query.data == "support":
        await query.message.reply_text(
            f"📞 Support:\n{SUPPORT}"
        )

    elif query.data == "language":
        await query.message.reply_text(
            "🌐 Language: English / বাংলা\n\nComing Soon..."
        )

    elif query.data == "checker":
        await query.message.reply_text(
            "🛡 MB Checker\n\nComing Soon..."
        ) 
      
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ ZENX IP BOT Started Successfully...")
    app.run_polling()


if __name__ == "__main__":
    main()
