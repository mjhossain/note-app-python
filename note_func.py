import json
import sys

# Reading json files
def loadNote():
    try:
        with open('notes.json') as f:
            data = json.load(f)
            return data
    finally:
        f.close()
    

# Adding a new note
def addNote(data):
    loadedData = loadNote()
    dublicateCount = 0
    for d in loadedData:
        if data['title'] in d['title']:
            # print('Dublicate found')
            print(d['title'])
            dublicateCount += 1
    if dublicateCount == 0:
        loadedData.append(data)
        writeFile(loadedData)
        print('\n\nnote added!')
    else:
        print('title already exists!')

# Save file
def writeFile(newData):
    try:
        with open('notes.json', 'w') as f:
            json.dump(newData, f)
            # print('note added!')
    finally:
        f.close()


#  Listing notes
def listNotes():
    loadedData = loadNote()
    print('\nID\tTitle\n')
    for data in loadedData:
        print(str(loadedData.index(data)) + '\t' + data['title'])
    print()


# Removing a note
def removeNote(taskID):
    loadedData = loadNote()
    itemIndex = None
    for data in loadedData:
        if taskID == loadedData.index(data):
            itemIndex = loadedData.index(data)
    if(itemIndex != None):
        loadedData.pop(itemIndex)
        writeFile(loadedData)
        print('note removed!')
    else:
        print('no such note!')
    # listNotes()


# View a note
def viewNoteByID(noteID):
    loadedData = loadNote()
    rNote = None
    for note in loadedData:
        if noteID == loadedData.index(note):
            rNote = note
    if(rNote != None):
        print('\nTitle: ' + rNote['title'] + '\n\n' + rNote['body'] + '\n\n')
    else:
        print('note not found!')   



