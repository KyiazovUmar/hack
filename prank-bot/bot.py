from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from user_data import user_chat_ids

BOT_TOKEN = '7461480911:AAF7CcvwU03m5npGWYWXRZ1P7fHJOv1VGJk'  # Replace this

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = '@' + (update.effective_user.username or update.effective_user.first_name)
    chat_id = update.effective_chat.id

    user_chat_ids[username] = chat_id
    print(f"Saved {username} → {chat_id}")

    prank_link = f"http://localhost:5000/?by={username}"

    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "This bot is for pranking friends. It does not violate Telegram rules.\n\n"
            f"Send this link to your friends 😈:\n{prank_link}"
        )
    )
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Bot is running... Waiting for messages.")
app.run_polling()
