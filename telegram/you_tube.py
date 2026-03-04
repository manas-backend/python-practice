import os
import uuid
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from pytube import YouTube

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! YouTube linkini yuboring, men videoni yuklab beraman 🎬")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Video yuklanmoqda... ⏳")

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        # Unique fayl nomi bilan yuklash
        file_path = stream.download(filename=f"{uuid.uuid4()}.mp4")

        # Video yuborish
        with open(file_path, "rb") as video_file:
            await update.message.reply_video(video_file)
        
        os.remove(file_path)

    except Exception as e:
        await update.message.reply_text(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    print("Bot ishga tushdi...")
    app.run_polling()
    
def normalize_youtube_url(url):
    if "/shorts/" in url:
        video_id = url.split("/shorts/")[1].split("?")[0]
        return f"https://www.youtube.com/watch?v={video_id}"
    return url