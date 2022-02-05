import pymysql

# DAO : Data Access Object DB를 사용해서 데이터를 조회하거나 조작하는 기능을 전담하도록 만든 오브젝트
class PyMyDao:


    def __init__(self):
        pass

    def getIlParking(self):
        MYSQL_CONN = pymysql.connect(host='localhost', port=3306, user='root', password='aksen5466!', db='parking', charset='utf8')
        db_data = []
        cursor = MYSQL_CONN.cursor()

        sql = "SELECT * FROM illegal LIMIT 200"
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            temp = {'address':row[1], 'count':row[2], 'year':row[3], 'lat':row[4], 'lng':row[5]}
            db_data.append(temp)

        MYSQL_CONN.commit()
        MYSQL_CONN.close()
        return db_data

# 잘 불러와지는지 태스트 코드
if __name__ == '__main__':
    base = PyMyDao()
    db_data_list = base.getIlParking()
    print(db_data_list)


