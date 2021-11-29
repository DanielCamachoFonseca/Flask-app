#Instanciamos el objeto mysql
import pymysql.cursors

mysql = pymysql.connect(host='localhost', port=3306, user='root', passwd='', database='ejemplo-db-flask')


