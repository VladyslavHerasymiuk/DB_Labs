class Order(object):
	def __init__(self, product_id, order_id, order_date, products):
		if not products.exists(product_id):
			raise Exception("Product not found!!!")
		self.product_id = product_id
		self.order_id = order_id
		self.order_date = order_date
		
		
	def __str__(self):
		return "product_id= %s, order_id=%d, order_date=%s" % (self.product_id, self.order_id, self.order_date)