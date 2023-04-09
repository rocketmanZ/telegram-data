import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace YOUR_TOKEN with your Telegram Bot token
bot = telegram.Bot(token='ADD_TOKEN')

# Start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! This is a test bot.")

# Echo message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Create the Updater and attach the handlers
updater = Updater(token='ADD_TOKEN', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling()

# Send data both ways
bot.send_message(chat_id='CHAT_ID', text='Hello, World!')
updates = bot.get_updates()
for update in updates:
    print(update.message.text)

# Stop the bot
updater.stop()