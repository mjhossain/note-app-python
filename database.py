import mysql.connector as mysql

# Connecting to Database
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root_pwd",
    database="py-note-app"
)

def viewNotes():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notes")
    results = cursor.fetchall()
    for record in results:
        print('\n\nTitle: {0} \t\t Created: {1} \n\n{2}\n\n'.format(record[1], record[3], record[2]))
        

    