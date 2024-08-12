#prismiquesupport and 7224124452:AAHcaXyO9HEgDkoeo2Ozy2xYgI_x6jMsiyg
import logging
import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

#Load envirenment variables .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Slack Bot User OAuth Token
SLACK_TOKEN = os.getenv('SLACK_BOT_TOKEN')

# The ID of your Slack channel
SLACK_CHANNEL_ID = 'C06RM0L0U94'  # Ensure this is the correct channel ID

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Send a greeting message
    await update.message.reply_text("Hi! How can I assist you today?")

# Function to handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    username = user.username if user.username else user.first_name
    message_text = update.message.text
    message_time = update.message.date.strftime("%Y-%m-%d %H:%M")  # Format date and time

    # Send acknowledgment to the user
    await update.message.reply_text("Thank you for your message. One of our representatives will reach out to you directly :)")

    # Prepare the message for the Slack channel
    slack_message = (
        f"Telegram > @{username}: 💬 {message_text}"
     
    )

    # Send the message to the Slack channel
    send_message_to_slack(slack_message)

def send_message_to_slack(message: str) -> None:
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SLACK_TOKEN}',
    }
    data = {
        'channel': SLACK_CHANNEL_ID,
        'text': message,
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        if response.status_code != 200 or not response_data.get("ok"):
            logger.error(f"Failed to send message to Slack: {response_data.get('error')}")
        else:
            logger.info(f"Message successfully sent to Slack: {message}")
    except Exception as e:
        logger.error(f"Exception occurred while sending message to Slack: {e}")

# Main function to start the bot
def main() -> None:
    # Create the Application
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()






























#OLD CODE BUT WORKS WITH SLACK
# import logging
# import requests
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# # Set up logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Your bot token from BotFather
# TOKEN = '7224124452:AAHcaXyO9HEgDkoeo2Ozy2xYgI_x6jMsiyg'

# # Slack Bot User OAuth Token
# SLACK_TOKEN = 'xoxb-6723292175280-7554986797124-LjaJxZoVVDp1HkMfHqzIjCfg'

# # The ID of your Slack channel
# SLACK_CHANNEL_ID = 'C06RM0L0U94'

# # Function to handle incoming messages
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user = update.effective_user
#     username = user.username if user.username else user.first_name
#     message_text = update.message.text
#     message_time = update.message.date.strftime("%Y-%m-%d %H:%M")  # Format date and time

#     # Send acknowledgment to the user
#     await update.message.reply_text("Thank you for your message. One of our representatives will reach out to you directly :)")

#     # Prepare the message for the Slack channel
#     slack_message = (
#         f"We received a new message from @{username} at {message_time}\n"
#         f"*The message:* 💬 {message_text}"
#     )

#     # Send the message to the Slack channel
#     send_message_to_slack(slack_message)

# def send_message_to_slack(message: str) -> None:
#     url = 'https://slack.com/api/chat.postMessage'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {SLACK_TOKEN}',
#     }
#     data = {
#         'channel': SLACK_CHANNEL_ID,
#         'text': message,
#     }
#     try:
#         response = requests.post(url, headers=headers, json=data)
#         response_data = response.json()
#         if response.status_code != 200 or not response_data.get("ok"):
#             logger.error(f"Failed to send message to Slack: {response_data.get('error')}")
#     except Exception as e:
#         logger.error(f"Exception occurred while sending message to Slack: {e}")

# # Main function to start the bot
# def main() -> None:
#     # Create the Application
#     application = ApplicationBuilder().token(TOKEN).build()

#     # Register the message handler
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     # Start the Bot
#     application.run_polling()

# if __name__ == '__main__':
#     main()













# Code from telegram bot to telegram channel! 
# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# # Set up logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Your bot token from BotFather
# TOKEN = '7224124452:AAHcaXyO9HEgDkoeo2Ozy2xYgI_x6jMsiyg'

# # The username of your support channel
# SUPPORT_CHANNEL_USERNAME = '@prismiquesupport'

# # Function to handle incoming messages
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user = update.effective_user
#     username = user.username if user.username else user.first_name
#     message_text = update.message.text
#     message_time = update.message.date.strftime("%Y-%m-%d %H:%M") 

#     # Send acknowledgment to the user
#     await update.message.reply_text("Thank you very much for your message. One of our assistants will reach you out very soon! 💗")

#     # Prepare the message for the support channel
#     support_message = (
#         f"We received a new message from @{username} at {message_time}\n"
#         f"The message:  💬{message_text}"
#     )
    
#     f"New message from {username} at {message_time}:\n\n{message_text}"

#     # Send the message to the support channel
#     await context.bot.send_message(chat_id=SUPPORT_CHANNEL_USERNAME, text=support_message)

# # Main function to start the bot
# def main() -> None:
#     # Create the Application
#     application = ApplicationBuilder().token(TOKEN).build()

#     # Register the message handler
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     # Start the Bot
#     application.run_polling()

# if __name__ == '__main__':
#     main()
