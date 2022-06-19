# gmed

Для запуска:
pip 22
python 3.10

Запуск локального дев сервера Django - python manage.py runserver 0.0.0.0:8000

запустить локально: docker-compose up --build

пуш в ветку server автоматом разворачивается и доступен по урлу https://gmed.terranout.mine.nu/

При изменении модели бд необходимо:
1. сформировать дельту изменений - python manage.py makemigrations
2. выполнить миграцию изменений в бд - python manage.py migrate 

Для удалённого доступа к бд из локальной джанги необходимо прокинуть IP хоста - 85.113.55.84 db

Структура проекта:
1. visor - основной модуль, временно хранящий не распределённую часть модели бд
2. predict - модуль нейросети; модель DotList, Coordinates
3. math_method - модуль вычисления параметров; модель ParametersList, Diagnoses, Parameters