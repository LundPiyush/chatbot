from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Initialize Bot
bot = ChatBot('Bot')

# Initialize Trainer
trainer = ListTrainer(bot)

BASE_DIR = os.path.dirname(os.path.realpath((__file__)))

path = os.path.join(BASE_DIR, 'data', 'english')

# Read datasets for training
for files in os.listdir(path):
	data = open(os.path.join(path, files), 'r').readlines()
	trainer.train(data)


# Interact with user
while True:
	message = input('You: ')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Bot: ', reply)
	if message.strip() == 'Bye':
		print('Bot: Bye')
		break
