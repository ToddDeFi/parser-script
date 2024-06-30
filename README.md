# parser-script

1. mkdir <название папки>
2. cd <название папки>
3. git clone https://github.com/ToddDeFi/parser-script.git
4. python3 -m venv venv
6. source venv/bin/activate
7. pip install -r requirements.txt
8. python listener.py


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
