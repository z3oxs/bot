import discord
from discord.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv, find_dotenv
import datetime
from datetime import date, datetime

load_dotenv(find_dotenv())
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')

from pymongo import MongoClient
cluster = MongoClient(f'mongodb+srv://{user}:{password}{host}')
db = cluster['codify']
conta = db['conta']
logs = db['logs']

class Tarefas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        @tasks.loop(hours=24)
        async def send_status():
            hr = datetime.now()
            logs.find_one_and_update({'_id': 0}, {'$set': {'last_ping': hr}})
        send_status.start()


def setup(bot):
    bot.add_cog(Tarefas(bot))