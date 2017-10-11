class products(object):
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
		
	def exists(self, aid):
		for product in self.products:
			if product_id == product.product_id:
				return True
		return False
	
	def __str__(self):
		return "\n".join(str(product) for product in self.products)
