# Very much a work in progress...


import pymysql
db = pymysql.connect(host='212.1.211.146', port=3306, user='sweb_mainapp', passwd='###P##6long',db='sweb_gamehub')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM blackjack WHERE ID=1")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % str(data))

# disconnect from server
db.close()
