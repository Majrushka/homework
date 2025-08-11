# Создайте асинхронную функцию fetch_multiple_urls(urls), которая:
# - Делает конкурентные GET-запросы к списку URL (используйте aiohttp или httpx).
# - Возвращает ответы в том же порядке, что и URL. 

# Пример:
# urls = ["https://example.com", "https://google.com"]
# results = await fetch_multiple_urls(urls)  # [response1, response2]

import asyncio
import aiohttp

async def fetch_multiple_urls(urls):
    # Создаём сессию для HTTP-запросов
    async with aiohttp.ClientSession() as session:
        # Создаём список задач (каждый URL — отдельный запрос)
        tasks = []
        for url in urls:
            # Добавляем задачу на GET-запрос к URL
            task = session.get(url)
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        return responses

async def main():

    urls = [
        "https://github.com/Majrushka?tab=repositories",
        "https://www.youtube.com/watch?v=btuxcr7Sxw4&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd",
        "https://flibusta.is/",
        "https://traveling.by/news/item/1617",
        "https://www.pinterest.com/"
    ]

    responses = await fetch_multiple_urls(urls)
    print(responses)

asyncio.run(main())