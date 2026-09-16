# Сайт для кондитерской SweetChest

Главная страница сайта кондитерской с адаптивной вёрсткой под 1920px, 1440px и 1024px, слайдером отзывов, созданным через `Swiper.js` и бэкендом на `Flask` с отправкой писем через сервис `Resend`.

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Запуск

Проект подготовлен для деплоя на сервере с `qunicorn`, ниже представлен пример запуска локально.

### Пример локального запуска

```
>>>python app.py

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 506-539-813

 >>>
```

После захода человека на сайт в командной строке может высветиться множество сообщений по типу:
```
127.0.0.1 - - [16/Sep/2026 19:53:09] "GET /static/Images/Catalog/img9.png HTTP/1.1" 304 -
```
Они не являются ошибкой, а, наоборот, свидетельствуют о корректной работе программы. Их иожно игнорировать.

### Цель проекта

Код написан в образовательных целях.