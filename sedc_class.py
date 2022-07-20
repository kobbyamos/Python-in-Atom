class sedc:
    def __init__(self, first_name, last_name, age, research_topic):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.research_topic = research_topic

#creating methods
    def research(self):
        #print(user1.research_topic, " is the research area of", user1.last_name)
        #print(user2.research_topic, " is the research area of", user2.last_name)
        #replacing with a generic code
        print(self.research_topic, " is the research area of", self.last_name)

    def fullname(self):
        print('The full name is {} {}'.format(self.first_name,self.last_name) )

user1 = sedc("Amos", "Boampong", 32, "Ferroelectrics")
user2 = sedc("Min", "Kim", 27, "Bilayer")

#print(user1.last_name, "is the oldest in SEDC lab")
#print(user2.last_name, "is the actual leader of SEDC lab")
#user1.research()
user2.research()
user1.fullname()
user2.fullname()
print(user1.last_name, "is sick")
print('{} {}'.format(user1.first_name,user1.last_name) )
