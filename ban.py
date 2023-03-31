import telegram
import csv

# Replace the following with your own Telegram API key and channel name
api_key = 'BOTFATHER API'
channel_name = 'GENIUS'

# Initialize the Telegram bot using the API key
bot = telegram.Bot(api_key)

# Retrieve the latest messages from the channel
messages = bot.get_chat_history(chat_id='@' + channel_name)

# Save the messages to a CSV file
with open('report.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Message'])
    for message in messages:
        writer.writerow([message.date.strftime('%Y-%m-%d %H:%M:%S'), message.text])

       FOR FREE
