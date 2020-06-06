import database as db
import sys
import note
from os import system, name
import argparse
from optparse import OptionParser

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def displayHelp():
    print("""
    Personal Note App

    Usage:      app.py [option]
    

    Options:
    add         Add a note
    rm          Remove a note (Usage: app.py rm -id 7)
    list        List all notes
    open        View a note (Usage: app.py open -id 2)

    Arguments:
    -id      Note id (required for rm option)
    """)

if __name__ == '__main__':
    if(sys.argv[1] == 'add'):
        note.createNote()
    elif(sys.argv[1] == 'list'):
        db.viewAllNotes()
    elif(sys.argv[1] == 'rm'):
        if(len(sys.argv) == 4):
            db.deleteNote(sys.argv[3])
        else:
            print('\nUsage of rm: app.py rm -id 4\n')
    elif(sys.argv[1] == 'open'):
        if(len(sys.argv) == 4):
            db.viewNoteByID(sys.argv[3])
        else:
            print('\nUsage of open: app.py open -id 4\n')
    else:
        displayHelp()


