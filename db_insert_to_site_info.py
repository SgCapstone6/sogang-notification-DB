import pymysql
import csv
host_name = ''
user_name = ''
password = ''
db_name = ''

with open("personal_data.txt","r",newline='') as input:
    host_name = input.readline()[:-1]
    user_name = input.readline()[:-1]
    password = input.readline()[:-1]
    db_name = input.readline()[:-1]

db = pymysql.connect(host = host_name, port =3306,
        user = user_name,
        passwd = password,
        db = db_name,
        charset = 'utf8')

fir = False
try:
    with db.cursor() as cursor:
        sql = 'TRUNCATE TABLE site_info'
        cursor.execute(sql)
        sql =( 'INSERT INTO site_info '
        '(site_layer_1,site_layer_2,site_layer_3,site_url,tag_id) '
        'VALUES (%s, %s,%s,%s,%s)')

        with open('data.csv',"r",encoding = 'utf-8',newline='') as csvfile:
            string = csv.reader(csvfile,delimiter=',')
            for row in string:
                if fir is False:
                    fir = True
                    continue
                temp =  '0' if row[5] == '' else row[5]
                cursor.execute(sql,(row[1],row[2],row[3],row[4],temp))

        db.commit()
finally:
    db.close()

