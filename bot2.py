import config 
import telebot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def default_test(message):
	keyboard = types.InlinekeyboardMarkup()
	url_button = types.InlinekeyboardButton(text="ЕХАЛА", url="https://m.twitch.tv/dangerlyoha/home")
	keyboard.add(url_button)
	bot.send_message(message.chat.id, "фака макака", reply_markup=keayboard)
