import mysql.connector as mysql

# Connecting to Database
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root_pwd",
    database="pythonTest"
)

# Creating a Cursor
cursor = db.cursor()

# Making Query
cursor.execute("SELECT * FROM users")

# Fetching Data
records = cursor.fetchall()

# Printing Data
for record in records:
    name = record[1]
    username = record[2]
    print(name + " " + username)
    
    
def say(msg):
    print(msg)