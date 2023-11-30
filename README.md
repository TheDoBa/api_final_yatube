#Описание 
## Открытый доступ к вашему API: разрешить CORS

Сделаем так, чтобы к вашему приложению можно было обращаться с любых доменов: настроим открытый доступ к вашему API.

Настроить CORS в Django-проекте можно с помощью библиотеки [django-cors-headers](https://github.com/adamchainz/django-cors-headers). Для этого установите пакет _django-cors-headers_ в виртуальном окружении:

Скопировать кодPYTHON

```
(venv)...$ pip install django-cors-headers 
```

Подключите его в _settings.py_ как приложение:
