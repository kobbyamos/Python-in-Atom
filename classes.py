'''class person():
    def _init_(self,age,weight,height, last_name):
        self.age = age
        self.weight =weight
        self.height = height
        self.last_name = last_name


user = person(25,80,177,"Boampong")

print(user.last_name)'''

import mymodule
from datetime import timedelta

mymodule.greeting("Boampong")
delta = timedelta(
        days = 50,
        seconds = 27,
        microseconds =10,
)

delta
