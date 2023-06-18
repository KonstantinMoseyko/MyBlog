# MyBlog

Блог с возможностью регистрации и публикации статей.

## Stack
[![Flask][Flask]][Flask-url]


## Инструкция
1. Клонируйте репозиторий
```sh
git clone https://github.com/KonstantinMoseyko/MyBlog.git
```
2. Создайте виртуальное окружение
```shell
python3 -m venv ./venv
```
3. Скопируйте и переименуйте .env.template в .env
```sh
cp .env.template .env
```
4. Активиркйте виртуальное окружение
```shell
source venv/bin/activate
```
5. Установите зависимости
```shell
pip install -r requirements.txt
```
6. Инициализируйте БД и создайте миграции. Создадим теги для статей и дефолтного админа.
```shell
flask db init
flask db migrate
flask db upgrade
flask create-tags
flask create-admin
```
7. Запустите приложение
```shell
python3 wsgi.py
```









<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Flask]: https://img.shields.io/badge/flask-778876?style=for-the-badge&logo=flask&logoColor=black
[Flask-url]: https://palletsprojects.com/p/flask/