# PerevalApi
***
## Описание
PerevalApi это API созданное для туристов, чтоб облегчить задачу по отправке данных о перевале.
Пользователями приложения, для которого создается PerevalApi являются горные туристы. В горах они должны вносить данные о перевале в приложение и отправлять их в ФСТР(Федерации Спортивного Туризма России), как только появится доступ в Интернет. 

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

Реализованные методы:
- submitData/ - добавление перевала туристом
- submitData/&lt;id&gt; - получение перевала по его __id__, а также возможность редактировать его
- GET api/submitData/?user__email=str:email - возможность отфильтровать перевалы по email
- swagger/ - реализована документация для каждого метода, используя swagger
*** 
## Установка
1. ### Клонирование репозитория
```commandline
git clone "https://github.com/AliakseiYafremau/PerevalApi"

```
2. ### Создание виртуального окружения
```commandline
python -m venv venv
```
3. ### Активация окружения
```commandline
venv/Scripts/activate
```
4. ### Установка зависимостей
```
pip install -r PerevalApi/requirements.txt
```
5. ### Вход в основную папку проекта
```commandline
cd PerevalApi
```
6. ### В данной папке создайте файл .env и добавьте в неё переменные для связи с ваше базой данных PostgreSQL
```text
FSTR_DB_HOST=<your_host>
FSTR_DB_PORT=<your_post>
FSTR_DB_LOGIN=<your_login>
FSTR_DB_PASS=<your_password>
```
7. ### Вход в корневую папку проекта
```commandline
cd perevalapi
```
8. ### Запуск проекта
```commandline
python manage.py runserver
```
*** 
## Пример работающего приложения [REST-API](http://alekseiyafremau.pythonanywhere.com/)(Устарело)