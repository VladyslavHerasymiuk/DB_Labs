import sys, os
from products import Products
from orders import Orders
from product import Product
from order import Order
from datetime import datetime
import pickle

products = Products()
orders = Orders()
menu_actions  = {}  
memoryP = []
memoryO = []
index = 0

def main_menu():
    os.system('clear')
    print ("Please choose the menu you want to start:")
    print ("1. Show products")
    print ("2. Enter products ")
    print ("3. Edit product ")
    print("4. Delete product")
    print("====================")
    print ("5. Show orders")
    print ("6. Make an order")
    print ("7. Edit order")
    print("8. Delete order")
    print("00. Search")
    print("11. pickle dump")
    print("22. pickle load")
    print ("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return
 
def pickle_dump():
    output = open('data.pkl', 'wb')
    pickle.dump(products, output)
    output1 = open('data1.pkl', 'wb')
    pickle.dump(orders, output1)
    output1.close()
    output.close()
    back()

def pickle_load():
    global products
    global ln
    global orders
    pkl_file = open('data.pkl', 'rb')
    data = pickle.load(pkl_file)
    pkl_file1 = open('data1.pkl', 'rb')
    data1 = pickle.load(pkl_file1)
    pkl_file1.close()
    pkl_file.close()
    products = data
    orders = data1
    ln = orders.len()
    exec_menu('9')
    return 


def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
 
def create_product(product_id, price, category):
    productC = Product(product_id, price, category)
    products.add(productC)

def create_order(product_id, order_id, order_date):
    try:
        orderC = Order(product_id, order_id, order_date, products)
        orders.add(orderC)
    except Exception:
        print("Product not found!!!")
    
def show_orders():
    print (orders)
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def menu1():
    print (products)
    print ("9. Back")
    print ("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

def menu2():
    print("If you admin, please, create products:")
    admin = str(input("Are you admin?(Yes/No): "))
    if admin == "Yes":
        ln = products.len()
        while(True):
            if ln not in memoryP:
                     print("product id: ", ln)
                     p = int(input("price: "))
                     c = str(input("category: "))
                     if c not in memoryP:
                         create_product( ln , p , c)
                         memoryP.append(c)
                         memoryP.append(ln)
                         break
                     else:
                          print("Сategory already created!!! You can't add >1 products to category!!!")
                          continue
                     
            else: 
                ln += 1
                continue  
    else:
        print("You aren't admin!!!")
        exec_menu(str(9))
    print("2. Next product")
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return

def make_an_order():
    global ln 
    while(True):
        if ln not in memoryO:
            while(True):
                p_id = int(input("product id: "))
                if not products.exists(p_id):
                    print("Product not found!!!")
                    break
                if orders.existP(p_id):
                    print("Product is bought!!!")
                    continue
                print("order id: ", ln)
                now = datetime.strftime(datetime.now(), "%Y-%m-%d")
                print("Date: ", now)
                create_order( p_id , ln , now)
                memoryO.append(ln)  
                print("Would you like to buy more?(Y/N)")
                ch = input(" >>  ")
                if ch == "N":
                    ln += 1
                    break
                elif ch == 'Y':
                    continue
            break
        else: 
            ln += 1
            continue
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return


def edit():
  while True:
    id = int(input("Enter product_id which you want to edit: "))
    if not products.exists(id):
            print("Product not found!!!")
            continue
    break
  try:
        pr = int(input("Enter new price, if you want to edit to: "))
  except Exception:
        pr = ''
  ct = str(input("Enter new category, if you want to edit to: "))
  if pr == '' and ct == '':
        products.edit_product(id)
  elif pr == '':
        products.edit_product(id, None, ct)
  elif ct == '':
        products.edit_product(id, pr, None)
  else:
         products.edit_product(id, pr, ct)

  print ("9. Back")
  print ("0. Quit" )
  choice = input(" >>  ")
  exec_menu(choice)
  return

def edit_O():
    orders.edit_order()
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)

def del_O():
    id = int(input("Enter order: "))
    if not orders.exists(id):
        print("Order not found!!!")
        print ("9. Back")
        print ("0. Quit" )
        choice = input(" >>  ")
        exec_menu(choice)
    else:
        print("Order DEL!")
        orders.delete(id)
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return
        
   

def delete():
    print("If you admin, please, delete products:")
    admin = str(input("Are you admin?(Yes/No): "))
    if admin == "Yes":
        while True:
            id = int(input("Enter product_id: "))
            if not products.exists(id):
                print("Product not found!!!")
                continue
            print("Product DEL!")
            products.delete(id)
            break
    else:
        print("You aren't admin!!!")
        exec_menu(str(9))
    print("4. Next product")
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return

def search():
    products.return_id(orders)
    print ("9. Back")
    print ("0. Quit" )
    choice = input(" >>  ")
    exec_menu(choice)
    return

def back():
    menu_actions['main_menu']()
 
def exit():
    sys.exit()
 

menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': edit,
    '4': delete,
    '5': show_orders,
    '6': make_an_order,
    '7': edit_O,
    '8': del_O,
    '9': back,
    '0': exit,
    '00':search,
    '11': pickle_dump,
    '22': pickle_load,
}

if __name__ == "__main__":
    ln = 0
    main_menu()