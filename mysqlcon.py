import pymysql


def conn():
    try:
        db=pymysql.connect('localhost','root','root','sec')

    except Exception as e:
        print(e)
    return db


