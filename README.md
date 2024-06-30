<img width="1440" alt="Снимок экрана 2024-06-30 в 17 29 34" src="https://github.com/ToddDeFi/parser-script/assets/102527508/abbb1294-0df1-4990-942a-61cb1f721245"># parser-script

1. mkdir <название папки>
2. cd <название папки>
3. git clone https://github.com/ToddDeFi/parser-script.git
4. python3 -m venv venv
6. source venv/bin/activate
7. pip install -r requirements.txt
8. python listener.py

Получение API ключа и хэша:
1.Log in to your Telegram core: https://my.telegram.org.
2.Go to "API development tools" and fill out the form.
3.You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.


Настройка словаря каналов: В файле скрипта, в секции конфигурации, укажите список каналов, которые вы хотите мониторить:

channels = ['@script_for_misha', '@another_channel'] 

Настройка словаря ключевых слов: 
В файле скрипта, в секции конфигурации, укажите список ключевых слов для фильтрации сообщений. Примерный формат словаря:  
filter_keywords = [
    'dollar',
    'bitcoin',
]  

Для удобства можно использовать ChatGPT для проверки формата и учёта опечаток/искажений слов: 
filter_keywords = [
    'dollar', 'dollars', 'usd',
    'bitcoin', 'btc',
] 
