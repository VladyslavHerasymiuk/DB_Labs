class Product(object):
	def __init__(self, product_id, price, category):
		self.product_id = product_id
		self.price = price
		self.category = category

	def __str__(self):
		return "product_id=%d, price=%d, category=%s" % (self.product_id, self.price, self.category)