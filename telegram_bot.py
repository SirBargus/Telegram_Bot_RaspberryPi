#!/usr/bin/python3
import requests
#Simple Telegram Bot Api

_token = None 
_url = None

def getMe():
	return requests.get(_url + "/getMe")

def getUpdates (offset = None, limit = None, timeout = None):
	args = {}
	if offset:
		args['offset'] = offset 
	if limit:
		args['limit'] = limit
	if timeout:
		args['timeout'] = timeout
	return requests.post(_url + "/getUpdates", params=args)

def sendMessage(chat_id, text, disable_web_page_preview = None, \
		reply_to_message_id = None, reply_markup = None):
	args = {'chat_id': chat_id, 'text': text}
	if disable_web_page_preview:
		args['disable_web_page_preview'] = disable_web_page_preview
	if reply_to_message_id:
		args['reply_to_message_id'] = reply_to_message_id
	if reply_markup:
		args['reply_markup'] = reply_markup
	return requests.post(_url + "/sendMessage", params=args)

def forwardMessage(chat_id, from_chat_id, message_id):
	args = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 
			'message_id': message_id}
	return requests.get(_url + "/forwardMessage", params=args)

def config(token):
	global _token
	global _url
	_token = token
	_url = "https://api.telegram.org/bot" + _token;


