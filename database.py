import mysql.connector as mysql
import time as time

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
    cursor.close()
        
def createNote():
    cursor = db.cursor()
    date = time.strftime('%Y-%m-%d %H:%M:%S')
    insert_query = "INSERT INTO notes(note_title, note_text) VALUES('from py', 'insert done from py')"
    cursor.execute(insert_query)
    db.commit()
    print(cursor.rowcount, "Note added")
    cursor.close()    