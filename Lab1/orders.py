from products import Products

class Orders(object):
	def __init__(self):
		self.orders = []

	def add(self, order):
		self.orders.append(order)

	def delete(self, order_id):
		ind = -1
		for index, order in enumerate(self.orders):
			if order.order_id == order_id:
				ind = index
		if ind > -1: 		
			self.orders.pop(ind)

	def exists(self, order_id):
		for order in self.orders:
			if order_id == order.order_id:
				return True
		return False

	def search(self, p_id):
		for order in self.orders:
			if p_id == order.product_id:
				print(p_id)
		
	def existP(self, p_id):
		for order in self.orders:
			if p_id == order.product_id:
				return True
		return False

	def len(self):
		len = 0
		for index, order in enumerate(self.orders):
			len = index + 1
		return len


	def edit_order(self):	
		return print("You can't edit your order!!!")

	def __str__(self):
		return "\n".join(str(order) for order in self.orders)