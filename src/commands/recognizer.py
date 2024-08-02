from mubble import Dispatch, Message

from src.rules import IsVoice
from src.utils import download_file, recognize_audio

dp = Dispatch()


@dp.message(IsVoice())
async def recognizer(message: Message):
    voice = message.voice.unwrap()
    file_id = voice.file_id
    file_ = (await message.ctx_api.get_file(file_id=file_id)).unwrap()
    file_path = file_.file_path.unwrap()
    file_bytes = await download_file(file_path)

    m = await message.answer("🎤 Beginning to recognize...")
    text = f"🎤 «{recognize_audio(file_bytes).capitalize()}»"
    await m.unwrap().edit(text)
