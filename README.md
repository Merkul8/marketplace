Доброго времени суток!
В данном репозитории представлен проект, выполненный с помощью django.
Проект представляет собой маркетплейс. Используемые технологии: Python, Django, PostgreSQL, DRF, Celery, Redis, JS - основные.

Старт проекта:
Предпочтительно использовать docker для работы с приложением, под него все настроено. Необходимо выполнение нескольких команд:

1) docker-compose build в корневой директории(место нахождения docker-compose.yml)
2) docker-compose up
3) После успешной инициализации проекта выполнить миграции "docker exec -it marketplace-web-1 python manage.py migrate"
!!!Рекомендуется!!!
4) "docker exec -it marketplace-web-1 python manage.py loaddata roles.json" загрузить данные для пользователей(их роли)
5) "docker exec -it marketplace-web-1 python manage.py loaddata categories.json" загрузить категории для товаров(если необходимо, например для тестирования)

Создание суперпользователя:
"docker exec -it marketplace-web-1 python manage.py createsuperuser"
