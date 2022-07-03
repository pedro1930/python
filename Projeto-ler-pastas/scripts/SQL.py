import psycopg2
import sys

#argumentos
database = sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
host=sys.argv[4]
port=sys.argv[5]
#conexão
conn = psycopg2.connect(
   database=database, user=user, password=password, host=host, port=port)
cursor = conn.cursor()
sql = '''----'''
cursor.execute(sql)