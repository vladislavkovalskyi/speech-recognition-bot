from mubble import MessageRule
from mubble.bot.dispatch.context import Context
from mubble.bot.rules.abc import Message


class IsVoice(MessageRule):
    async def check(self, message: Message, ctx: Context) -> bool:
        return bool(message.voice and message.voice.unwrap())
