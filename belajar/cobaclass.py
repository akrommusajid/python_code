class student:
	def __init__(self, name, branch, year):
		self.name = name
		self.branch = branch
		self.year = year
		print("A student was created")

	def print_details(self):
		print("Name : ", self.name)
		print("Branch : ", self.branch)
		print("Year : ", self.year)

if __name__ == '__main__':
	main()