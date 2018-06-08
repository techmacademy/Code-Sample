class Dog(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def bark(self, bark):
		print(bark)

	def walk(self, speed):
		print("I'm walking at",speed, "mph")

	def __str__(self):
		return 'Instance of Dog'
