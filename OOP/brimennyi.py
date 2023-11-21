1 Создать виртуальное окружения 
python3 -m venv <venv>
2Устанавливаем нужные библиотеки и джанго
 pip instsill<library>
pip


5 записать наше предложения в installed app в настройках (подключения вашего приложения в проект)
6 Настройка базы данных
DATABASES = {
 'default':{
  'ENGINE':"django.db.backends.postgresql",
  'NAME':'<name+of_your_db>'
  'USER':'<mahabat>'
  'PASSWORD':"<1>",
  'HOST':'localhost'
  'PORT':5432
 }
}
7 создания базы данных в псстгрес
8 работва смиграцией
python3 manage.py makemigrations
