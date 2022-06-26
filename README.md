## TechnicalSupportAssistantBot
Бот предназначен для осуществления технической поддержки клиентов. Бот умеет отвечать на часто задаваемые вопросы клиентов.
## Запуск бота локально
Для запуска бота на вашем сервере необходимо выполнить следующие действия:

1. Cоздать бота в Телеграмм  [см.тут](https://core.telegram.org/bots).
2. Инициализировать с вашим ботом чат.
3. Склонировать себе файлы репозитория выполнив команду **git clone https://github.com/AloneRD/TechnicalSupportAssistantBot.git**.
4. Установить необходимы зависимости **pip install -r requirements.txt**.
5. В директории с проектом создать файл **.env** со следующим содержимом:
 ```
    TELEGRAM_TOKEN=cvbfdk8945453
    VK_TOKEN=dfgdfghdfghdfgh
    TG_CHAT_ID=433434
    GOOGLE_APPLICATION_CREDENTIALS=credo.json"
 ```
   - **VK_TOKEN** токен для доступа к API ВКонтакте
   - **TELEGRAM_TOKEN** токен к вашему телеграмм боту
   - **TG_CHAT_ID** id чата, в который бот будет посылать логи
   - **GOOGLE_APPLICATION_CREDENTIALS** json ключ для доступа к API Google [см.тут](https://cloud.google.com/docs/authentication/getting-started)
7. запустить бота :
   * Для запуска телеграмм бота **.\bot.py**
   * Для запуска бота Вконтакте **.\VK_bot.py**

## Демо ботов
**Бот Вконтакте**

https://vk.com/public214174985

![bandicam 2022-06-26 20-24-00-679](https://user-images.githubusercontent.com/39197265/175826372-eb09b973-f3b3-4a2e-bd1b-f2be3bcc9ba9.gif)

**Бот Телеграмм**

https://web.telegram.org/k/#@TechnicalSupportAssistantBot

![bandicam 2022-06-26 20-21-12-721](https://user-images.githubusercontent.com/39197265/175826295-4d5c41eb-e275-4c84-b1a7-09e541b397e0.gif)


## Дополнительная информация

Бот был создан с использованием DialogFlow.
Чтобы не создавать новые Intents руками был написан скрипт, который сделает это за вас
Команда для запуска скрипта 
```
.\create_new_intent.py --project-id gfghfnt-uwyu --file-path questions.json

  --project-id - id проекта в DialogFlow
  --file-path - путь к фалу с обучающим контентом 
```

Пример содержания файла questions.json
```
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    }
    }
```
