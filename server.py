#!/usr/bin/python3
import time
import telegram_bot
import json
from subprocess import Popen, PIPE, STDOUT

def config():
	with open('config.json') as data_file:
		data = json.load(data_file)
		global _token, _user_id
		_token = data['token']
		_user_id = data['user_id']

def execute(command):
	if "/torrent start" == command:
		command = "sudo service transmission-daemon start"
	elif "/torrent stop" == command:
		command = "sudo service transmission-daemon stop"
	try:
		out = Popen(command.split(' '), stdout=PIPE, stderr=STDOUT)
		return out.stdout.read()
	except:
		return "Something wront happened with your message :(."


if __name__ == "__main__":
	config()
	telegram_bot.config(_token)
	
	last = 0

	while True:
		update = telegram_bot.getUpdates(offset=last)
		if update.status_code == 200:
			data = json.loads(update.text)
			for i in data['result']:
				if i['message']['from']['id'] == _user_id:
					res = execute(i['message']['text'])
					if res == b'':
						res = "OK."
				else:
					res = "Wrong user"
				telegram_bot.sendMessage(i['message']['chat']['id'], res, \
						disable_web_page_preview = True, \
						reply_to_message_id = i['message']['message_id'])
				if last <= i['update_id']:
					last = i['update_id'] + 1

