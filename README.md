This is a simple note taking app using python.

There is 2 version to it: 

    MySQL:
        Using mysql as a database (inside mysql-db-app) 

    JSON:
        Using JSON to store files. (index)


App Usage:

    Create a Note:
        python note.py add
    
    List all Notes:
        python note.py list
    
    Open a Note: (get note id from list)
        python note.py open -id 1 
    
    Remove a Note: (get note id from list)
        python note.py rm -id 1