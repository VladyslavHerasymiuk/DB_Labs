from products import Products
from orders import Orders
from product import Product
from order import Order

products = Products()
orders = Orders()

def create_product(product_id, price, category):
	productC = Product(product_id, price, category)
	products.add(productC)

def create_order(product_id, order_id, order_date, products):
	orderC = Order(product_id, order_id, order_date, products)
	orders.add(orderC)

create_product(1, 200, "ee")
create_product(2, 1, "kdsek")

'''a = int(input())
print("++++++++")
b = int(input())
print("++++++++")
c = str(input())
print("++++++++")'''


create_product(int(input())),int(input()),str(input())



print(products)
print(orders)
products.return_id(orders)
'''
print author1
print "authors:"
print authors

book1 = Book(1, 1, "B1", authors)
print book1

books = Books()
books.add(book1)

try:
	book2 = Book(10, 1, "B1", authors)
except Exception:
	print "Error creating book2"
	
#books.add(book2)
print "books:"
print books
'''