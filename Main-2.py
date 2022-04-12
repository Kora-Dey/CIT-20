import random

#Reads all items from wizard_all_items.txt
def read_items( ):
  file = '/Users/sdey/Documents/wizard_all_items.txt'
  all_items  = []
  with open(file) as wfile:
      for item in wfile:
        all_items.append(item.strip())
  return  all_items   

#Reads all items from wizard_inventory.txt    
def read_inventory():
  file = '/Users/sdey/Documents/wizard_inventory.txt'
  w_list = []
  try:
    with open(file) as wfile:
      for item in wfile:
        w_list.append(item.strip())
  except FileNotFoundError:
    w_list = []
  return w_list
  
#Updates wizard_inventory.txt
def write_inventory(w_list):
  file = '/Users/sdey/Documents/wizard_inventory.txt'
  with open(file,"w") as wfile:
    for item in w_list:
      wfile.write('%s\n'% item)
    
def walk( ):      
    all_items  = read_items()
    wizard_list = read_inventory()
    random_item = random.choice(all_items)
    item_count = len(wizard_list)
    print('While walking down a path, you see ',random_item)
    choice = input('Do you want to grab it? (y/n):')
    if choice == "y" and item_count < 4 :
       wizard_list.append(random_item)
       write_inventory(wizard_list)
       print("You picked up"+random_item)
    elif choice == "y" and item_count >= 4:
      print("You cannot carry any more items. Drop something first.")

      
#Shows all items in the inventory
def show():
  wizard_list = read_inventory()
  i = 0
  for item in (wizard_list):
    print(str(i+1)+". "+ item)
    i = i+1

#Drops one item from the inventory
def drop( ):
  wizard_list = read_inventory()
  if len(wizard_list) == 0:
    print('You have nothing to drop')
  index = int(input("Number:"))
  if index > len(wizard_list) or index < 1:
    print("Invalid input")
  else:
    item = wizard_list[index-1]
    wizard_list.remove(item)
    write_inventory( wizard_list)
    print('You dropped', item, ".")
      
#Displays the application title
def display_title( ): 
  print('The Wizard Inventory program')
  print()

def display_menu(): 
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()
    
def main( ):
  display_title()
  display_menu()
  while True:
    print()
    command = input('Command:')
    if command == "exit":
      print("Thank you for using my app")
      break
    elif command == "walk":
        walk()
    elif command == 'show' :
      show()
    elif command == 'drop' :
      drop()
    else:
      print('wrong command.')
    

main()  

