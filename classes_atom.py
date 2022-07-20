class person:
    def __init__(self, age, weight, height, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.last_name = last_name

    def walk(self):
        print("i am walking away")

    def run(self):
        print("Its now time to run away")

user = person(25, 80 , 177, "Boampong" )

print(user.last_name)
print(user.age)
user.walk()
user.run()
