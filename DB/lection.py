# PostgreSQL - система управления базами данных(СУБД,DBMS)
# Это ряд программ  и инструментов позволяющий создавать БД управлять ею и манипулировать данными внутри(CRUD)
# Postgres - сама база данных оба обьекно реляционна то есть данные хранятся в виде таблиц и таблицы имеют связь
#  между собой
# SQL(Structured Query Language) декларативный язык структрурированных запросов он применяется для  слздания и 
# получения данных при помощи запросов в БД(())
#-------------------------------------------------
#команда для входа 
# \q
# exit
# создания суперюзера 
# CREATE ROLE "USERNAME" SUPERUSER LOGIN PASSWORD'1';
# создания бд 
# CREATE DATABASE 'NAME';
# \L - список всех бд
# \du - все юзеры
# \dt - все таблицы(нужно подключить к бд заранее)
# \d 'name' - подробная информация про таблицу (нужно подключится  к бд заранее)
# бд- база данных
# \с 'name' - команда для подключения в бд 
#----------------------
# Типы полей в Postgresql
# Numeris Types(чuсловые)

 # a.smallint(2 bytes) -> -32767 to 32767
 # b.integer(4 bytes) -> -2.147...to 2.147
 # c.bigint(8 bytes) -> ...
 # d.real(4 bytes) -> число в плавающей точкой вещественное
 # f. double precsion (8 bytes)-> real но только с двойной точностью
 # d. serial(4 bytes)-> int auto-increment(автоматически заполняется)
 # Character types (символы типы(строковые))
 # a. varhar(кол-во символов)- если мы укажем 50 символов а заполним тоько 10 то остальное будет свободною MAX255
 # b. char(кол-во символов)- если укажем 50 символов а запомним только 10 осьальные будут заполненны пробелом Max 255
 # c. text()- неограниченное кол-во символов
 # Boolean Type
#  a. boolean(1 byles)- True/False 
# data - календарная дата(год.месяцюдень)
# location - координатная точка (x,y)-(245, -12)
# enumerate types ;
# ('a','b', 'c')
#CREATE TYPE <any name> AS ENUM('Happy','Sad','Mad');
# Ограничения:
#1. NOT NULL OБЯЗАТЕЛЬНО К ЗАПОЛНЕНИЮ
#@ UNIQUE ТО что будут хранится только уникальные данные
#3 CHECK -> CHECK age> -1 ограничения проверки на условия
#4 PRIMARY KEY(для установки индетификаторов данных в таблице)
#5 FOREIGN KEY (ДЛЯ УСТАНОВКИ СЗЯЗЕЙ МЕЖДУ ТАБЛИЦАМИ)
#6 ON DELETE ДЛЯ УСТАНОВКИ ПЕВЕДЕНИЯ ПРИ УДАЛЕНИИ ДАННЫХ КОТОРЫЕ БЫЛИ СЗЯЗАНЫ
# ЭСПОРТ  вд(дамп)
# pg_dump -u <username> _d 'dbname' > 'file.sql'
# Ипорт:
# psql -U<username> -d <dbname> =f <filename>

#SELECT count(product_name), c.category_name FROM products as p,categories as c WHERE p.category_id = c.category_id GROUP BY c.category_name;
# сортирует таблицу ао кол во категориям
# создания бд
# CREATE DATABASE 'name';имеен рекомендательный характер(recomended)
# create database 'name';
# команда для создания таблицы
# CREATE TABLE [<constraint>]
# <colymn><type>[<constraint>]],
# )
# CREATE TABLE films(
#   code char(5),
#   title varchar(100),
#   date date,
#   genre varchar(50),
#   budget bigin,
#   country varchar(50)
# );

# DROP TABLE <name> - удаление таблицы
# КАМАНДА ДЛЯ ДОБАВЛЕНИЯ ДАННЫХ В ТАБЛИЦУ
# INSERT INFO <tablename> -(colums) VALUEA(data), (data);
#INSERT INFO  filims(code, title, date, genre, budjet, country)V



#каманда для обновления 
# UPDATE <table> SET <column> = <new_value> WHERE <column> = <value>;
# UPDATE films SET genre = 'Adventure' WHERE code='het5';
# команда для удаления
# DELETE FROM <table> WHERE <column> = <value>;
#QRDER BY ;ПОЗВОЛЯЕТ НАМ СОРТИРОВАТЬ ВЫВОДЯЩИЕ ДАННЫЕ ПО УБЫВАНИЮ ИЛИ ВОЗРАСТАНИЮЮ ASC(ПО ВОЗРАСТАНИЮ
# И DESC( ПО УБЫВАНИ)
# Синтаксиз  SELECT <row> FROM <tablename> ORDER BY <row>[ASC/DESC]
# WHERE:используются для фильтрации по полям будут выводтися только те данные которые соответсвуют условию оператора WHERE
# Синтаксиз:SELECT <row> FROM <tablename> WHERE <row> =чему либо;
# BETWEEN:УСЛОВИЯ МЕДЖУ 
# SELECT * FROM filims WHERE id BETWEEN 3 AND  

# LIKE :ВЫВОДИТ РЕЗУЛЬТАТ КОТОРЫЙ СООТВЕТСТВУЕТ ВВЕДЕННОМУ ШАБЛОНУ ДЛЯ СТОКЮ
# чувствителен  к регистру
# ILIKE: тоже самое не зависит от регистра
# # Синтаксиз SELECT<row> FROM <tablename> WHERE <row> LIKE/ILIKE чему либо:
# JOIN :ВЫБОРКА  данных из двух таблиц соединения таблиц
# LEFT JOIN ВЫБорка  будет содержать все строки из левой таблицы
# RIGHT JOIN выборка будет содержать свк строки из правой таблицы
# SELECT p1.title,p1.price.o1.quantity,p1.price * o1.quantity as
# total_sum FROM PRODUCTS p1 JOIN order o1 ON p1.id= o1.product_id
