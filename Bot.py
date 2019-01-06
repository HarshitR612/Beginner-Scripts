#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 01:22:58 2019

@author: frodo612
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Lisa')
bot.set_trainer(ListTrainer)

for files in os.listdir('/home/frodo612/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english') :
	data = open('/home/frodo612/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
	bot.train(data)

while True :
	message = input('User: ')
	reply = bot.get_response(message)
	print('ChatBot :', reply)

	if message.strip() == 'Goodbye' :
		print('ChatBot : Bye')
		break