# File updatedb.py: update Person object on database
import shelve
db = shelve.open('persondb')               # Reopen shelve with same filename
##for key in sorted(db):                     # Iterate to display database objects
##    print(key, '\t=>', db[key])            # Prints with custom format
##sue = db['Sue Jones']                      # Index by key to fetch
##sue.giveRaise(.10)                         # Update in memory using class's method
##db['Sue Jones'] = sue                      # Assign to key to update in shelve
##db.close()      

for key in sorted(db):
    person = db[key]
    person.giveRaise(0.1)
    db[key] = person
    print(key, '\t=>', db[key])
db.close()
