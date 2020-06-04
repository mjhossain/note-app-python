import database as db
import sys
import note
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# db.viewNotes()
# db.createNote('My Name', 'Hi I am Mohammed')
# db.viewAllNotes()
# db.viewNoteByID(6)
# db.deleteNote(5)

# msg = sys.stdin.read()
# print(msg)

# note.createNote()
clear()
# db.viewNoteByID(7)
# note.appendNote(7)
db.viewAllNotes()

