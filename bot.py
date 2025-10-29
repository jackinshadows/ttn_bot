from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import asyncio
import os

# === Налаштування ===
TOKEN = "8404246224:AAGTrWXTqoFgt4Xe2OiPWMNX91oOdBsYcEc"
GROUP_ID = -1003118858109

bot = Bot(token=TOKEN)
dp = Dispatcher()

# === Функція: обробка отриманого файлу ===
@dp.message()
async def handle_doc(message: types.Message):
    if message.document:
        file_name = message.document.file_name
        file_path = f"received/{file_name}"
        os.makedirs("received", exist_ok=True)

        # Завантажуємо файл локально
        await bot.download(message.document, file_path)

        # Хто відправив
        sender = message.from_user.full_name

        # Відправляємо копію у групу
        doc = FSInputFile(file_path)
        caption = f"Від: {sender}\nФайл: {file_name}"

        await bot.send_document(chat_id=GROUP_ID, document=doc, caption=caption)

        # Підтвердження менеджеру
        await message.reply("✅ ТТН успішно відправлено у групу!")

# === Запуск бота ===
async def main():
    print("🤖 Бот запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())