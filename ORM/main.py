# ORM(objekt-Retalional Mapping)-технология програмирования благодаря которой работтчики могут использовать язык програмировая для 
# взаимодейстькии с реляционной баззой данных(PostreSQL, MySQL,OracleDB)Вместо того чтобы  писать сыпые запросы на оператора SQL 
# вы будете писать код ООП на языке програмирования это очень сильно ускоряет разработку приложения и бд
#  на начальных

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database='orm_db',
    user='mahabat',
    password='1',
    host='localhost',
    port=5432,
)

# print(db.connect())


