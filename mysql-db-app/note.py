import sys
import database as db

def createNote():
    print('\n\n\t\t Create a Note\n\n')
    title = input('Note Title: ')
    print('\nPress Ctrl+D (Mac) & Ctrl+Z (Win) to save & exit. \n')
    noteBody = sys.stdin.read()
    db.createNote(title, noteBody)

def appendNote(nodeID):
    note = db.getNoteBody(nodeID)
    print('Title: ', note['title'])
    print('\n',note['body'])
    print('------- Add Below -------')
    print('\nPress Ctrl+D (Mac) & Ctrl+Z (Win) to save & exit. \n')
    newNoteBody = sys.stdin.read()
    print('\n--------- Updating Note ----------\n')
    noteBody = note['body'] + '\n' + newNoteBody
    db.updateNote(nodeID, noteBody)


    

