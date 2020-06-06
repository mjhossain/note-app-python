import sys
import note_func as note
from os import system, name
import argparse
from optparse import OptionParser

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def addNote():
    print('\nAdd Note\n')
    title = input('Title: ')
    print('\nPress Ctrl+D (Mac) & Ctrl+Z (Win) to save & exit. \n')
    body = sys.stdin.read()
    data = {'title': title, 'body': body}
    note.addNote(data)

def displayHelp():
    print("""
    Personal Note App

    Usage:      note.py [option]
    

    Options:
    add         Add a note
    rm          Remove a note (Usage: note.py rm -id 7)
    list        List all notes
    open        View a note (Usage: note.py open -id 2)

    Arguments:
    -id      Note id (required for rm option)
    """)

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        displayHelp()
    else:
        if(sys.argv[1] == 'add'):
            addNote()
        elif(sys.argv[1] == 'list'):
            note.listNotes()
        elif(sys.argv[1] == 'rm'):
            if(len(sys.argv) == 4):
                noteID = int(sys.argv[3])
                note.removeNote(noteID)
            else:
                print('\nUsage of rm: app.py rm -id 4\n')
        elif(sys.argv[1] == 'open'):
            if(len(sys.argv) == 4):
                noteID = int(sys.argv[3])
                note.viewNoteByID(noteID)
                # print(sys.argv[3])
            else:
                print('\nUsage of open: note.py open -id 4\n')
        else:
            displayHelp()



