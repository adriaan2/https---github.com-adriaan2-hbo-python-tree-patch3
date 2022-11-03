'''
Create an application that manages contacts in an addressbook. The following requirements should be implemented:
- Add a contact with first name and last name (only alphabet), multiple (unidue) e-mails (containing at least one '@'), 
  multiple (unidue) phone numbers (only digits). Also, an ID should be generated which should be 1 higher than the highest current ID.
- Remove a contact by ID.
- List all contacts with the option to sort by first_name or last_name (default first_name) with a sort_by parameter 
  and in ascending (ASC) or decending (DESC) direction (default ASC) witb a direction parameter.
- Merge duplicate contacts (automatically). Contacts with the exact same full name (first and last name combined) should be merged. 
  The e-mails and phone numbers of the duplicate contacts should be added to the the first duplicate contact (contact with the highest ID). 
  The other duplicate contcts should be deleted from the addressbook.
- Contacts are read from the provided JSON file and should be updated with new or removed contacts.
'''



import os
import sys
import json

addressbook = []


'''
print all contacts in the following format:
======================================
Position: <position>
First name: <fname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''
def display():
    for i in addressbook:
        print("position",i["id"])
        print("fname",i["first_name"])
        print("lastname",i["last_name"])
        print("email",i["emails"])
        print("phonenumbers",i["phone_numbers"])

'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''
def list_contacts():
    pass
  
'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''
def add_contact():
    id=len(addressbook)+1
   
    fname=input("fname ")    
    lastname=input("lastname ")  
    phone_number=input("phonenumber ")
    if "," in phone_number:
         phone1,phone2 =str.split(phone_number,",")
         phonedict=[phone1,phone2]
    else:
             phonedict=[phone_number]

    mail=input("email ")
    maildict=[]
    if "," in mail:
        mail1,mail2=str.split(mail,",")
        maildict=[mail1,mail2]
    else :
        maildict=[mail]
    
    newcontact={
        'id':id,
        'first_name':fname,
        'last_name':lastname,
        'phone_numbers':phonedict,
         'emails':maildict

    }     
    addressbook.append(newcontact)
     
def remove_contact():
     
    
    
 
  temp = int(input())
  for i in addressbook:
        if i["id"]==temp:
            addressbook.remove(i)
            

         

      

''''
merge duplicates (automated > same fullname [fname & lastname])
'''
def merge_contacts():
   print(addressbook)
   for i in addressbook:
     for j in addressbook:
        if i["id"]!=j["id"]:
          if i["first_name"]==j["first_name"]:
            if i["last_name"]==j["last_name"]:
                i["phone_numbers"]+=j["phone_numbers"]
                addressbook.remove(j)
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





def main(json_file):
    read_from_json(json_file)
    while True:
        user_choice=input("[L]list contact\n[A]add contact\n[M]merge contact\n[R]remove\n[Q]quit\n").upper()
        if user_choice=="A":
            add_contact()
            
        elif user_choice=="R":
            remove_contact()
        elif user_choice=="M":
            merge_contacts()
        elif user_choice=="L":
            display()
        elif user_choice=="Q":
            write_to_json(json_file)
            print("close program")
            break
        
        
    
if __name__ == "__main__":
    main('contacts.json')