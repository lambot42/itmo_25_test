# ITMO Master Programs Bot

Простой чат-бот для VK Teams, который помогает абитуриенту разобраться в магистерских программах ITMO: "AI" и "AI Product". Бот парсит актуальные учебные планы с сайта университета, отвечает на вопросы по этим программам, и рекомендует выборные дисциплины с учетом бэкграунда пользователя.

## Как запустить

1. Установите зависимости:
   pip install -r requirements.txt

2. Запустите бота:
   python bot.py

3. Укажите адрес http://<ваш_ip>:8000/webhook в настройках Webhook вашего VK Teams бота.

## Как работает

- Бот автоматически скачивает учебные планы программ AI и AI Product с сайта ITMO.
- В ответ на вопрос определяет выбранную программу, выдает часть учебного плана или рекомендует выборные дисциплины по профилю.
- Если вопрос не по теме — сообщает, что работает только с магистратурами AI и AI Product.

## Пример запросов

- "Покажи учебный план AI"
- "Посоветуй выборные дисциплины по бизнесу для AI Product"
- "Чем отличается AI от AI Product?"