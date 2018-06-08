class Dog(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def describe(self, bark):
		print(bark)

	def __str__(self):
		return 'Instance of Dog'