import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='ciation-v1',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()


def search(keyword=None):
    keyword = "%" + keyword + "%"
    cursor.execute("SELECT * FROM papers WHERE title LIKE %s", keyword)
    papers = cursor.fetchall()
    return papers
