menu_items = {}

def add_menu_item(item):
  menu_items[item.lower()] = 0

def initialize_menu():
  add_menu_item("Wings")
  add_menu_item("Cookies")
  add_menu_item("Spring Rolls")

  add_menu_item("Salmon")
  add_menu_item("Steak")
  add_menu_item("Meat Tornado")
  add_menu_item("A Literal Garden")

  add_menu_item("Ice Cream")
  add_menu_item("Cake")
  add_menu_item("Pie")

  add_menu_item("Coffee")
  add_menu_item("Tea")
  add_menu_item("Unicorn Tears")

def process_input(user_input):
  input_lower = user_input.lower()
  if input_lower in menu_items:
    menu_items[input_lower] += 1
    if menu_items[input_lower] > 1:
      print(f'{menu_items[input_lower]} orders of {user_input} has been added to your meal.')
    else:
      print(f'{menu_items[input_lower]} order of {user_input} has been added to your meal.')
  else:
    print('That item is not on the menu, but we can make it for you for an additional 50% surcharge.')

def review_order():
  print ('''
************************************
**         Your Order:            **
************************************
  ''')
  orders = False
  
  for item, count in menu_items.items():
    if count == 1:
      print(f'{count} order of {item.capitalize()}')
      orders = True
    elif count >= 1:
      print(f'{count} orders of {item.capitalize()}')
      orders = True

  if not orders:
    print('No orders have been placed')

print ('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To view your order, type "order" **       
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
''')

def order_up():
  print ('''
***********************************
** What would you like to order? **
***********************************
  ''')
  
  user_input = input("> ")

  if user_input.lower() == 'quit':
    print('Quitting..')
    return
  elif user_input.lower() == 'order':
    review_order()
    order_up()
  else:
    process_input(user_input)
    order_up()

def init_program():
  initialize_menu()
  order_up()

init_program()