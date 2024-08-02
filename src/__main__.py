from mubble import API, Dispatch, Mubble, Token
from src import commands

dispatch = Dispatch()
dps = [*commands.dps]
for dp in dps:
    dispatch.load(dp)

bot = Mubble(
    api=API(Token.from_env(path_to_envfile=".env")),
    dispatch=dispatch,
)

bot.run_forever()
