from telegram import Bot
from config.env_vars import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

# Inicializar bot de Telegram
bot = Bot(token=TELEGRAM_TOKEN)

def send_telegram_message(message):
    """
    Envía un mensaje al canal de Telegram.
    """
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print(f"Error al enviar mensaje a Telegram: {e}")