import mysql.connector as mysql

# Connecting to Database
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root_pwd",
    database="py-note-app"
)

def viewNotes(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = {0}".format(id))
    results = cursor.fetchall()
    for record in results:
        print('\n\nTitle: {0} \t\t Created: {1} \n\n{2}\n\n'.format(record[1], record[3], record[2]))
    cursor.close()
        
def createNote(noteTitle, noteBody):
    cursor = db.cursor()
    insert_query = "INSERT INTO notes(note_title, note_text) VALUES('{0}', '{1}')".format(noteTitle, noteBody)
    cursor.execute(insert_query)
    db.commit()
    print(cursor.rowcount, "Note added")
    cursor.close()    
    
