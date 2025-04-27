# encoding:utf-8

from bot.bot import Bot
from bridge.context import Context
from bridge.reply import Reply


class ZeroBot(Bot):

    def __init__(self):
        super().__init__()

    def reply(self, query, context: Context = None) -> Reply:
        return None
