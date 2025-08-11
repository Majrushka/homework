# Напишите асинхронную функцию set_async_timer(seconds, callback), которая:
# - Ждёт указанное количество секунд (asyncio.sleep).
# - Вызывает callback функцию после завершения таймера.

# Пример:
# async def on_timer_end():
#   print("Таймер сработал!")

# await set_async_timer(2, on_timer_end) # Через 2 секунды: "Таймер сработал!"

import asyncio

async def set_async_timer(seconds, callback):
    await asyncio.sleep(seconds)
    await callback()
    
async def on_timer_end():
    print("Таймер сработал!!")

async def main():
    await set_async_timer(2, on_timer_end)

asyncio.run(main())