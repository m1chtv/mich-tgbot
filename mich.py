import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
import os

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "@YOUR_CHANNEL_ID"

PHOTO_PATH = "mich.png"

def create_caption():
    now = datetime.now()
    date_time = now.strftime("%Y/%m/%d %H:%M:%S")
    caption = f'<b>{date_time}</b>\n\n#NewProxy'
    return caption

def create_keyboard():
    keyboard = [
        [InlineKeyboardButton("Connect", url=""),
         
         InlineKeyboardButton("Connect", url="")],

        [InlineKeyboardButton("Connect", url=""),
         
         InlineKeyboardButton("Connect", url="")],

        #  [InlineKeyboardButton("Connect", url=""),
         
        #  InlineKeyboardButton("Connect", url="")],

        #  [InlineKeyboardButton("Connect", url=""),
         
        #  InlineKeyboardButton("Connect", url="")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def main():
    bot = Bot(token=BOT_TOKEN)
    
    photo_exists = os.path.exists(PHOTO_PATH)

    caption = create_caption()
    reply_markup = create_keyboard()

    try:
        if photo_exists:
            with open(PHOTO_PATH, 'rb') as photo:
                await bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=caption, reply_markup=reply_markup, parse_mode='HTML')
            print("Photo and message sent successfully!")
        else:
            await bot.send_message(chat_id=CHANNEL_ID, text=caption, reply_markup=reply_markup, parse_mode='HTML')
            print("Photo not found, but message sent successfully without photo!")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    asyncio.run(main())