class Products(object):
	def __init__(self):
		self.products = []
	
	def add(self, product):
		self.products.append(product)

	def delete(self, product_id):
		ind = -1
		for index, product in enumerate(self.products):
			if product.product_id == product_id:
				ind = index
		if ind > -1: 		
			self.products.pop(ind)

	def edit_product(self, product_id, price = None, category = None):
		if category is None:
			category = self.products[product_id - 1].category
		if price is None:
			price = self.products[product_id - 1].price
		ind = -1
		for index, product in enumerate(self.products):
			if product.product_id == product_id:
				ind = index
		if ind > -1: 		
			self.products[product_id - 1].price = price
			self.products[product_id - 1].category = category	

	def return_id(self, orders):
		for index, product in enumerate(self.products):
			if product.price >= 100:
				orders.search(product.product_id)

	def exists(self, product_id):
		for product in self.products:
			if product_id == product.product_id:
				return True
		return False

	def len(self):
		len = 0
		for index, product in enumerate(self.products):
			len = index + 1
		return len
	
	def __str__(self):
		return "\n".join(str(product) for product in self.products)
