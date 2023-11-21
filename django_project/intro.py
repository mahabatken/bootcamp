#1 Создать виртуальное окружение 
#         python3 -m venv(venv)


#2 Установить нужные библиотеки и джанго 
#         pip install<libary>
#         pip freeze > requirements.txt
#3 создание проекта и файла manage.python3
#         django-admin startaproject <name>

#4 создание приложения для проекта 
#         python3 manage.py startapp<name>
2#         django-admin startapp <name>

# 5 Записать название вашего приложения в   installed apps в настройках (подключение вашего приложения в проект)
# 6 настройка базы данных 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'firstapi_db',
#         'USER': 'adilet',
#         'PASSWORD': '1',
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }

# Создание базы данных в постгрес
# Работа с миграциями 
#     8.1 создвем файлы миграциями
#     python3 manage.py makemigration
#     8.2 запускаем файлы миграции

# запуск сервера 
    # python3 manage.py runserver
# создвние суперюзера
    # python3 manage.py createsuperuser