def view(contacts):
  index= int(input("Number:"))
  size = len(contacts)
  if index > size or index < 1:
      print("Invalid contact number. There are only",size,"contacts.")
  else:
      print("Name:"+contacts[index-1][0])
      print("Email:"+contacts[index-1][1])
      print("Phone:"+contacts[index-1][2])

def display_title():
  print( "Contact Manager")
  print()
 
def add(contacts):
    name = input("Name:")
    email= input("Email:")
    phone= input("Phone:")
    info=[]
    info.append(name)
    info.append(email)
    info.append(phone)
    contacts.append(info)
    print(name+" "+" was added.")

def delete(contacts):
    index = int(input("Number:"))
    if index > len(contacts) or index < 1:
      print(" invalid contact number")
    else:
      record = contacts[index-1]
      contacts.remove(record)
      print(record[0],"was deleted.")
  
def display(contacts):
  if len(contacts) == 0:
    print("No contacts")
  else:
    for i in range(len(contacts)):
      info = contacts[i]
      print( str(i+1)+"."+ info[0])
    
def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()

contacts = [["Guido van Rossum", "guido@python.org", "+31 0474 33 88 26"],
            ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]
      
def main():
    display_title():
    display_menu()
    while True:
      command = input('Command:')
      if command == "add":
         add(contacts)
         print()
      elif command == 'list' :
         display(contacts)
         print()
      elif command == "del":
         delete(contacts)
         print()
      elif command == "view":
         view(contacts)
         print()
      elif command == 'exit':
         print()
         print("Thank you for using my app")
         break
      else:
            print('wrong command.')

main()

