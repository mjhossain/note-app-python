import mysql.connector as mysql

# Connecting to Database
db = mysql.connect(
    host="localhost",
    user="root",
    passwd="root_pwd",
    database="py-note-app"
)

# Views all notes from db
def viewAllNotes():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM notes")
        results = cursor.fetchall()
        for record in results:
            print('\n\nID: {0} \t Title: {1} \t Created: {2} '.format(record[0], record[1], record[3]))
        cursor.close()
    except:
        print("DB error: viewNotes")
  
# Views single note by ID
def viewNoteByID(noteID):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM notes WHERE id = {0}".format(noteID))
        results = cursor.fetchall()
        for record in results:
            print('\n\nID: {0} \t Title: {1} \t Created: {2} \n\n{3}\n\n'.format(record[0], record[1], record[3], record[2]))
        cursor.close()
    except:
        print("DB error: viewNotes")
   

# Get note body Text
def getNoteBody(noteID):
    note = {}
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = {0}".format(noteID))
    result = cursor.fetchall()
    for record in result:
        note['id'] = record[0]
        note['title'] = record[1]
        note['body'] = record[2]
    cursor.close()
    return note


# Update Note
def updateNote(noteID, noteBody):
    cursor = db.cursor()
    update_query = "UPDATE notes SET note_text = '{0}' WHERE id = {1}".format(noteBody, noteID)
    cursor.execute(update_query)
    db.commit()
    cursor.close()
    print('Note updated!\n\n')
   
# Inserts note into db
def createNote(noteTitle, noteBody):
    # try:
    cursor = db.cursor()
    insert_query = "INSERT INTO notes(note_title, note_text) VALUES('{0}', '{1}')".format(noteTitle, noteBody)
    cursor.execute(insert_query)
    db.commit()
    print(cursor.rowcount, "Note added")
    cursor.close() 
    # except:
    #     print("DB error: createNote")  
 
 
# Deletes a single note with ID
def deleteNote(noteId):
    try:
        cursor = db.cursor()
        del_query = "DELETE FROM notes WHERE id = {0}".format(noteId)
        cursor.execute(del_query)
        db.commit()
        cursor.close()
        print('Note removed!')
    except:
        print("DB error")
    