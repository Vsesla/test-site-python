from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import DB

admins = [1561460389]                 # list of admin's IDs (for example - [345345234, 557546745, 745985797])
review_channel_url = 'https://t.me/feedbackhsh'     # url of the channel with feedbacks (for example:  https://t.me/+RDE2gELnj6A1NTRa)
review_channel_id = '-1003228499718'      # id of the channel with feedbacks (for example:   -1001627120479)
admin_ulr = '@Paravozikththth'              # admin's url

db = DB('db.db')            # database name

BOT_TOKEN = '8507118395:AAEnicXGkYVvcScXt_P2tP0tO4yBnVC051Q'              # bot's token
bot = Bot(BOT_TOKEN, parse_mode='html') 

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)