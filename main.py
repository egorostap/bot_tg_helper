from aiogram.utils import executor
from create_bot import dp


# объявление включения бота
async def on_startup(_):
  print('бот вышел в онлайн')

from handler import client, admin, other

# вызовы команд из файлов озер и клиент
client.registr_handlers_client(dp)
other.registr_handlers_other(dp)

# запуск поллинг
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)