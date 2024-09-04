# mich-tgbot
## Telegram Bot for Proxy Posting

This Python script automates the process of posting a proxy with a custom caption and inline buttons to a Telegram channel. It uses the `python-telegram-bot` library along with `asyncio` for asynchronous operations.

## Features:
- **Dynamic Captions:** The caption includes the current date and time.
- **Inline Keyboard:** Custom inline buttons can be configured to provide quick actions or links.
- **Photo Support:** Optionally attach a photo to the message, if available.
- **Error Handling:** Provides basic error handling to ensure the bot continues running smoothly.

## Setup:
1. **Install Dependencies:**
   ```bash
   pip install python-telegram-bot asyncio
   ```
2. **Configure Your Bot:**
- Replace `BOT_TOKEN` with your actual Telegram bot token.
- Set the `CHANNEL_ID` to the Telegram channel where the message should be sent.
- Update the `PHOTO_PATH` with the path to the image you want to send.

## Usage:
Run the script using:
```bash
python mich.py
```

**The bot will send a message to the specified Telegram channel, including an optional photo, dynamic caption, and inline buttons.**
