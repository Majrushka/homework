# Напишите асинхронную функцию fetch_url(url), которая:
# - Имитирует HTTP-запрос (используйте asyncio.sleep(1) вместо реального запроса).
# - Возвращает "данные" с URL (например, f"Data from {url}").
# Запустите параллельно запросы к 5 разным URL и соберите результаты.
# Ожидаемый результат:
# Все запросы выполняются параллельно, общее время ~1 секунда (а не 5 секунд).


import asyncio

async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = [
        "https://github.com/Majrushka?tab=repositories",
        "https://www.youtube.com/watch?v=btuxcr7Sxw4&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd",
        "https://flibusta.is/",
        "https://traveling.by/news/item/1617",
        "https://www.pinterest.com/"
    ]

    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

asyncio.run(main())