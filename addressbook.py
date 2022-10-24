'''
Create an application that manages contacts in an addressbook. The following requirements should be implemented:
- Add a contact with first name and last name (only alphabet), multiple (unique) e-mails (containing at least one '@'), 
  multiple (unique) phone numbers (only digits). Also, an ID should be generated which should be 1 higher than the highest current ID.
- Remove a contact by ID.
- List all contacts with the option to sort by first_name or last_name (default first_name) with a sort_by parameter 
  and in ascending (ASC) or decending (DESC) direction (default ASC) witb a direction parameter.
- Merge duplicate contacts (automatically). Contacts with the exact same full name (first and last name combined) should be merged. 
  The e-mails and phone numbers of the duplicate contacts should be added to the the first duplicate contact (contact with the highest ID). 
  The other duplicate contcts should be deleted from the addressbook.
- Contacts are read from the provided JSON file and should be updated with new or removed contacts.
'''

import email
import mailbox
import os
from readline import append_history_file
import sys
import json

addressbook = []


'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''
def display(list = []):
    ...


'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''
def list_contacts():
    ...

    return addressbook


'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''
def add_contact():
    
    firstname=input("firstname ")    
    lastname=input("lastname ")  
    phone_number=input("phonenumber ")
    mail=input("email")

    newcontact={
        
        'first_name':firstname,
        'last_name':lastname,
        'phone_numbers':phone_number,
         'emails':mail

    }     
     print(newcontact)


def remove_contact():
    pass


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''
def merge_contacts():
    ...


'''
read_from_json
Do NOT change this function
'''
def read_from_json(filename):
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        for contact in data:
            addressbook.append(contact)
         

'''
write_to_json
Do NOT change this function
'''
def write_to_json(filename):
    
    json_object = json.dumps(addressbook, indent = 4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


'''
main function:
build menu structure as following
the input can be case-insensitive (so E and e are valid inputs)
[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program
Don't forget to put the contacts.json file in the same location as this file!
'''

def main(json_file):
    read_from_json(json_file)
      
    

'''
calling main function: 
Do NOT change it.
'''








if __name__ == "__main__":
    main('contacts.json')
    user_choice=input("user_choice ")
    
    if user_choice=="a":
        add_contact()
    elif user_choice=="d":
        remove_contact()
    elif user_choice=="m":
        merge_contacts()
    elif user_choice=="l":
         list_contacts
      
